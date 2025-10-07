from typing import List, Dict, Any
import logging
import json

import mcp_tools.tool_llm_query as tool_llm_query
import mcp_tools.tool_file_manager as tool_file_manager
import mcp_tools.tool_code_assistant as tool_code_assistant
import mcp_tools.tool_data_processor as tool_data_processor
import mcp_tools.tool_web_researcher as tool_web_researcher
import mcp_resources.resource_conversation as resource_conversation
import mcp_resources.resource_document as resource_document
import mcp_resources.resource_system as resource_system
import mcp_resources.resource_analytics as resource_analytics
import mcp_prompts.prompt_code_review as prompt_code_review
import mcp_prompts.prompt_data_analysis as prompt_data_analysis
import mcp_prompts.prompt_technical_writer as prompt_technical_writer
import mcp_prompts.prompt_research_assistant as prompt_research_assistant

from mcp.server import Server
from mcp.types import Tool, Resource, Prompt
from mcp.server.lowlevel.helper_types import ReadResourceContents
from mcp.types import TextContent, PromptMessage, GetPromptResult

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-gateway")

def register_handlers(server: Server, db_path: str):
    """Register all MCP handlers"""

    # Tool handlers
    @server.list_tools()
    async def list_tools() -> List[Tool]:
        return [
            tool_llm_query.llm_query_tool,
            tool_file_manager.file_manager_tool,
            tool_code_assistant.code_assistant_tool,
            tool_data_processor.data_processor_tool,
            tool_web_researcher.web_researcher_tool
        ]


    @server.call_tool()
    async def call_tool(name: str, arguments: Dict[str, Any]):
        try:
            if name == "llm_query":
                return await tool_llm_query.handle_llm_query(arguments)
            elif name == "file_manager":
                return await tool_file_manager.handle_file_manager(arguments)
            elif name == "code_assistant":
                return await tool_code_assistant.handle_code_assistant(arguments)
            elif name == "data_processor":
                return await tool_data_processor.handle_data_processor(arguments)
            elif name == "web_researcher":
                return await tool_web_researcher.handle_web_researcher(arguments)
            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
        except Exception as e:
            logger.error(f"Tool {name} error: {e}")
            return [TextContent(type="text", text=f"Error: {str(e)}")]


    # Resource handlers
    @server.list_resources()
    async def list_resources() -> List[Resource]:
        return [
            resource_conversation.conversation_resource,
            resource_document.document_resource,
            resource_system.system_resource,
            resource_analytics.analytics_resource
        ]


    @server.read_resource()
    async def read_resource(uri: str):
        uri = str(uri)
        try:
            if uri == "mcp://gateway/conversations":
                data = await resource_conversation.get_conversations(db_path)
            elif uri == "mcp://gateway/documents":
                data = await resource_document.get_documents(db_path)
            elif uri == "mcp://gateway/analytics":
                data = await resource_analytics.get_analytics(db_path)
            elif uri == "mcp://gateway/system":
                data = await resource_system.get_system_status(db_path)
            else:
                raise ValueError(f"Unknown resource: {uri}")
            return [ReadResourceContents(content=json.dumps(data, indent=2, default=str), mime_type="text/plain")]
        except Exception as e:
            logger.error(f"Resource read error: {e}")
            return [ReadResourceContents(content=f"Try: {str(e)}", mime_type="text/plain")]


    # Prompt handlers
    @server.list_prompts()
    async def list_prompts() -> List[Prompt]:
        return [
            prompt_code_review.code_review_prompt,
            prompt_data_analysis.data_analysis_prompt,
            prompt_technical_writer.technical_writer_prompt,
            prompt_research_assistant.research_assistant_prompt
        ]

    @server.get_prompt()
    async def get_prompt(name: str, arguments: Dict[str, str]) -> GetPromptResult:
        try:
            if name == "code_review":
                prompt_text = await prompt_code_review.generate_code_review_prompt(arguments)
            elif name == "data_analysis":
                prompt_text = await prompt_data_analysis.generate_data_analysis_prompt(arguments)
            elif name == "research_assistant":
                prompt_text = await prompt_research_assistant.generate_research_prompt(arguments)
            elif name == "technical_writer":
                prompt_text = await prompt_technical_writer.generate_technical_writing_prompt(arguments)
            else:
                raise ValueError(f"Unknown prompt: {name}")

            return GetPromptResult(
                description=f"Generated {name} prompt",
                messages=[
                    PromptMessage(
                        role="user",
                        content=TextContent(type="text", text=prompt_text)
                    )
                ]
            )
        except Exception as e:
            logger.error(f"Prompt generation error: {e}")
            return GetPromptResult(
                description=f"Error generating {name} prompt",
                messages=[
                    PromptMessage(
                        role="user",
                        content=TextContent(type="text", text=f"Error: {str(e)}")
                    )
                ]
            )