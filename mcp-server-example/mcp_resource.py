import mcp_instance
import os

mcp = mcp_instance.mcp

@mcp.resource("http://localhost/kodex_academy")
def load_kodex_academy_details() -> str:
    """
    Load a text resource from resources/kodex_academy.txt.
    """
    path = os.path.join("resources", "kodex_academy.txt")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No knowledge base found. Add resources/kodex_academy.txt"
