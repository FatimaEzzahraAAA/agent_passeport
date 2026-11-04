import os
from dotenv import load_dotenv
from google import genai

# 1. Chargement de la clé API depuis le fichier .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Erreur : La clé API est introuvable. Vérifie ton fichier .env")

# 2. Initialisation du client Gemini
client = genai.Client(api_key=API_KEY)

print("Modèles disponibles pour génération de contenu :")
for m in client.models.list():
    if "generateContent" in m.supported_actions:
        print(f"- {m.name}")

# 3. Le System Prompt (rôle, ton, contraintes, few-shot)
SYSTEM_PROMPT = """Tu es un assistant expert en démarches administratives marocaines, spécialisé sur le passeport.
Ton rôle est d'aider les utilisateurs en fournissant des informations claires, précises et à jour.

RÈGLES STRICTES :
- Tu dois répondre UNIQUEMENT en te basant sur le contexte fourni.
- Si le contexte ne contient pas l'information, réponds poliment : "Je ne trouve pas cette information dans ma base de connaissances actuelle."
- Ne jamais inventer de délais, de prix ou de documents. Sois factuel.
- Si la question n'a aucun rapport avec le passeport marocain, refuse poliment de répondre.

EXEMPLE (Few-shot) :
Utilisateur : Quels sont les documents pour un premier passeport ?
Assistant : D'après les informations à ma disposition, il faut une pièce d'identité, un justificatif de domicile, des photos et le paiement de la taxe.
"""

# 4. Fonction pour faciliter les tests
def poser_question(question: str):
    print(f"\n👤 Utilisateur : {question}")
    print("🤖 Assistant (en réflexion)...")
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",# Modèle rapide et gratuit
        contents=[SYSTEM_PROMPT, question],
    )
    
    print(f"\n💬 Réponse : {response.text}")
    print("-" * 60)

# 5. Exécution des 3 questions test de l'exercice
if __name__ == "__main__":
    print("=== TEST DE L'ASSISTANT PASSEPORT ===")
    
    # Test 1 : Question dans le sujet
    poser_question("Quels sont les documents nécessaires pour renouveler un passeport ?")
    
    # Test 2 : Question piège (pour vérifier s'il hallucine un prix)
    poser_question("Quel est le prix exact du timbre fiscal pour un passeport ?")
    
    # Test 3 : Question hors-sujet (doit refuser poliment)
    poser_question("Comment obtenir un visa pour aller aux États-Unis ?")