import mcp_instance
import os

mcp = mcp_instance.mcp

@mcp.resource("http://localhost/codeauris")
def load_codeauris_details() -> str:
    """
    Load a text resource from resources/codeauris.txt.
    """
    path = os.path.join("resources", "codeauris.txt")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No knowledge base found. Add resources/codeauris.txt"
