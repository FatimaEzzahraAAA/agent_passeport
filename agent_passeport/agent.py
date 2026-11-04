import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp import StdioServerParameters

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

SYSTEM_PROMPT = """Tu es un assistant expert en démarches administratives marocaines sur le passeport.
Tu dois TOUJOURS utiliser l'outil 'retrieve' pour chercher les informations avant de répondre.
Si l'outil ne trouve pas l'information, dis poliment que tu ne sais pas."""

chemin_serveur = str(Path(__file__).resolve().parent / "serveur_mcp.py")

mcp_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=[chemin_serveur],
            env=os.environ.copy()  # <--- LA LIGNE MAGIQUE EST ICI
        ),
    )
)

root_agent = Agent(
    name="agent_passeport_adk",
    model="gemini-flash-latest",
    instruction=SYSTEM_PROMPT,
    tools=[mcp_toolset],
)