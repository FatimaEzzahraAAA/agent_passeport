import os
import time # <-- NOUVEAU : pour gérer les pauses
from dotenv import load_dotenv
from pinecone import Pinecone
from google import genai

# 1. Initialisation
load_dotenv()
client_google = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("demarchesmaroc-passeport")

# Liste des modèles à essayer (du plus récent au plus ancien)
MODELES_POSSIBLES = ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash", "gemini-2.5-flash"]

# --- FONCTION DE FALLBACK (Gestion des pannes) ---
def generate_content_avec_fallback(prompt, system_prompt=None):
    for modele in MODELES_POSSIBLES:
        try:
            contents = [system_prompt, prompt] if system_prompt else prompt
            response = client_google.models.generate_content(
                model=modele,
                contents=contents
            )
            return response.text # Succès, on retourne la réponse
        except Exception as e:
            if "503" in str(e) or "429" in str(e):
                print(f"⚠️ Modèle {modele} surchargé. Pause de 2s et on essaie le suivant...")
                time.sleep(2)
                continue
            else:
                raise e # Si c'est une vraie erreur, on arrête
    raise Exception("❌ Tous les modèles sont actuellement indisponibles. Réessayez plus tard.")

# --- QUESTION 8 : Fonction Retrieve ---
def retrieve(query: str, top_k: int = 5) -> list[str]:
    response = client_google.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
        config={'output_dimensionality': 768}
    )
    query_vector = response.embeddings[0].values
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    return [match.metadata["text"] for match in results.matches]

# --- QUESTION 9 : Prompt Final ---
SYSTEM_PROMPT = """Tu es un assistant expert en démarches administratives marocaines sur le passeport.
Ton rôle est de répondre aux questions des utilisateurs.

INSTRUCTION STRICTE :
- Réponds UNIQUEMENT à partir du contexte fourni ci-dessous.
- Si la réponse n'est pas dans le contexte, dis poliment : "Je ne trouve pas cette information dans ma base de connaissances actuelle."
- Ne jamais inventer de prix ou de délais.
"""

def poser_question_rag(question: str):
    print(f"\n👤 Utilisateur : {question}")
    
    contexte_chunks = retrieve(question, top_k=3)
    contexte = "\n\n---\n\n".join(contexte_chunks)
    
    prompt_final = f"""Contexte:
{contexte}

Question: {question}
"""
    
    print("🤖 L'IA cherche dans le contexte et répond...")
    # Utilisation de notre fonction de fallback
    reponse = generate_content_avec_fallback(prompt_final, SYSTEM_PROMPT)
    
    print(f"\n💬 Réponse : {reponse}")
    print("-" * 60)
    return contexte, reponse

# --- QUESTION 10 (BONUS) : Métrique Faithfulness ---
def evaluer_faithfulness(contexte, question, reponse_ia):
    prompt_juge = f"""
    Tu es un évaluateur strict. Voici une question, un contexte et une réponse générée par une IA.
    Est-ce que la réponse est ENTIÈREMENT justifiée et soutenue par le contexte fourni ? 
    Si la réponse contient des informations qui ne sont pas dans le contexte, réponds "NON".
    Si la réponse est bien basée sur le contexte, réponds "OUI".
    Ne donne que le mot "OUI" ou "NON".
    
    Contexte: {contexte}
    Question: {question}
    Réponse de l'IA: {reponse_ia}
    """
    reponse_juge = generate_content_avec_fallback(prompt_juge)
    return reponse_juge.strip()

# --- EXÉCUTION DES TESTS ---
if __name__ == "__main__":
    print("=== TESTS DE L'AGENT RAG (PARTIE B) ===")
    
    questions_test = [
        "Quels sont les documents nécessaires pour renouveler un passeport ?",
        "Quel est le prix exact du timbre fiscal pour un passeport ?",
        "Comment obtenir un visa pour aller aux États-Unis ?"
    ]

    for q in questions_test:
        try:
            contexte_utilise, reponse_generee = poser_question_rag(q)
            
            print("📊 Évaluation de la fidélité (Faithfulness) en cours...")
            score = evaluer_faithfulness(contexte_utilise, q, reponse_generee)
            print(f"➡️ La réponse est-elle fidèle au contexte ? {score}")
            print("=" * 60)
        except Exception as e:
            print(f"❌ Erreur : {e}")