import os
import glob
import time # <-- NOUVEAU : pour gérer les pauses
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from google import genai

# 1. Chargement des clés
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_KEY = os.getenv("PINECONE_API_KEY")

client_google = genai.Client(api_key=GEMINI_KEY)
pc = Pinecone(api_key=PINECONE_KEY)

INDEX_NAME = "demarchesmaroc-passeport"

# 2. Création de l'index s'il n'existe pas
if INDEX_NAME not in pc.list_indexes().names():
    print(f"Création de l'index {INDEX_NAME}...")
    pc.create_index(
        name=INDEX_NAME,
        dimension=768, 
        metric="cosine", 
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# NOUVEAU : On vide l'index pour éviter les doublons si on relance le script
print("Nettoyage des anciennes données...")
try:
    index.delete(delete_all=True)
except Exception:
    pass # Si l'index est vide, ça ne pose pas de problème

# 3. Fonction de Chunking avec Overlap
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap 
    return chunks

# 4. Traitement du corpus
print("Lecture du corpus...")
fichiers = glob.glob("corpus/*.txt")

if not fichiers:
    print("❌ Erreur : Aucun fichier trouvé dans le dossier 'corpus'.")
else:
    tous_les_chunks = []
    metadonnees = []
    
    for fichier in fichiers:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        
        url_source = f"https://demarchesmaroc.com/passeport/{os.path.basename(fichier)}"
        chunks = chunk_text(contenu)
        print(f"Fichier {os.path.basename(fichier)} découpé en {len(chunks)} chunks.")
        
        for i, chunk in enumerate(chunks):
            tous_les_chunks.append(chunk)
            metadonnees.append({"id": f"{os.path.basename(fichier)}-chunk-{i}", "source_url": url_source})

    print(f"\nGénération des embeddings pour {len(tous_les_chunks)} chunks au total...")
    
    batch_size = 40 # On réduit un peu la taille du lot pour être plus sûr
    vectors_to_upsert = []
    
    for i in range(0, len(tous_les_chunks), batch_size):
        batch = tous_les_chunks[i:i+batch_size]
        print(f"  -> Traitement du lot {i//batch_size + 1}...")
        
        # --- NOUVEAU : Gestion du Rate Limit (Erreur 429) ---
        try:
            response = client_google.models.embed_content(
                model="gemini-embedding-001",
                contents=batch,
                config={'output_dimensionality': 768}
            )
        except Exception as e:
            if "429" in str(e):
                print("    ⚠️ Limite d'API atteinte. Pause de 60 secondes pour laisser le quota se réinitialiser...")
                time.sleep(60) # On attend 1 minute
                print("    🔄 Reprise du traitement...")
                # On réessaie le même lot
                response = client_google.models.embed_content(
                    model="gemini-embedding-001",
                    contents=batch,
                    config={'output_dimensionality': 768}
                )
            else:
                raise e # Si c'est une autre erreur, on arrête tout
        
        # On récupère les vecteurs
        for j, embedding_obj in enumerate(response.embeddings):
            index_global = i + j
            vectors_to_upsert.append({
                "id": metadonnees[index_global]["id"],
                "values": embedding_obj.values,
                "metadata": {
                    "text": tous_les_chunks[index_global], 
                    "source_url": metadonnees[index_global]["source_url"]
                }
            })
        
        # Petite pause préventive entre chaque lot (5 secondes)
        time.sleep(5)

    # 5. Envoi vers Pinecone
    print(f"\nEnvoi des {len(vectors_to_upsert)} vecteurs à Pinecone...")
    for i in range(0, len(vectors_to_upsert), 50):
        batch = vectors_to_upsert[i:i+50]
        index.upsert(vectors=batch)

    print("✅ Indexation terminée avec succès !")