import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone
from google import genai
from mcp.server.fastmcp import FastMCP

# 1. Charger le .env du dossier parent de manière infaillible
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 2. Initialisation
client_google = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("demarchesmaroc-passeport")

mcp = FastMCP("demarchesmaroc-passeport")

@mcp.tool()
def retrieve(query: str, top_k: int = 5) -> str:
    """Recherche dans la base de connaissances les passages les plus pertinents pour répondre à la question de l'utilisateur (documents, procédures, délais, coûts concernant le passeport marocain)."""
    
    response = client_google.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
        config={'output_dimensionality': 768}
    )
    query_vector = response.embeddings[0].values
    
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    
    contexte = "\n\n---\n\n".join([match.metadata["text"] for match in results.matches])
    return contexte

if __name__ == "__main__":
    mcp.run()