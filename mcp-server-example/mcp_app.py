from mcp.server.fastmcp import FastMCP

import mcp_instance
import mcp_prompt
import mcp_resource
import mcp_tool

mcp = mcp_instance.mcp

if __name__ == "__main__":
    mcp.run(transport='stdio')
