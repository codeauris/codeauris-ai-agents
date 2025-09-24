import mcp_instance

mcp = mcp_instance.mcp

@mcp.prompt("user_greeting")
def user_greeting(name: str = "Learner"):
    """
    Simple MCP prompt to greet a user.
    """
    return f"Hello, {name}! Welcome to CodeAuris."
