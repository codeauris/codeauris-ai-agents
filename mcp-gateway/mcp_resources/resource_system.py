from typing import List, Dict, Any
from datetime import datetime

from mcp.types import Resource

from mcp_tools.tool_llm_query import llm_query_tool
from mcp_tools.tool_file_manager import file_manager_tool
from mcp_tools.tool_code_assistant import code_assistant_tool
from mcp_tools.tool_data_processor import data_processor_tool
from mcp_tools.tool_web_researcher import web_researcher_tool

system_resource = Resource(
                    uri="mcp://gateway/system",
                    name="System Status",
                    description="Current system status and configuration",
                    mimeType="application/json"
                )


async def get_system_status(db_path) -> Dict[str, Any]:
    """Get current system status"""
    return {
        "status": "running",
        "server_name": "MCP Gateway",
        "version": "1.0.0",
        "protocol_version": "2024-11-05",
        "capabilities": {
            "tools": len(await get_available_tools()),
            "resources": 4,
            "prompts": 4
        },
        "database_path": db_path,
        "timestamp": datetime.now().isoformat()
    }

async def get_available_tools() -> List[str]:
    """Get list of available tool names"""
    return [llm_query_tool.name, file_manager_tool.name, code_assistant_tool.name, data_processor_tool.name, web_researcher_tool.name]