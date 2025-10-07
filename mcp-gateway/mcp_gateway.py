import os
import asyncio
from dotenv import load_dotenv

# MCP Server SDK imports (install with: pip install mcp)
from mcp.server import Server
from mcp.server.stdio import stdio_server

from database_operations import init_database
from mcp_handlers import register_handlers

# import environment variables from .env file
load_dotenv()
LLM_TYPE = os.getenv("LLM_TYPE")
db_path = os.getenv("DB_FOLDER_PATH")

class MCPGatewayServer:
    def __init__(self):
        # Set environment variable programmatically
        os.environ["LLM_TYPE"] = LLM_TYPE

        self.server = Server("mcp-gateway")

        init_database()
        register_handlers(self.server, db_path)


async def main():
    """Main entry point for MCP server"""
    gateway = MCPGatewayServer()

    # Run the server using stdio transport (standard for MCP)
    async with stdio_server() as (read_stream, write_stream):
        await gateway.server.run(
            read_stream,
            write_stream,
            gateway.server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())