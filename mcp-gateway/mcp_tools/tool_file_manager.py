from typing import Any, Dict
import json
from mcp.types import Tool, TextContent
from llm_call_methods import simulate_llm_response
from database_operations import log_file_operation

file_manager_tool = Tool(
                    name="file_manager",
                    description="Manage files and directories with LLM-assisted operations",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "operation": {
                                "type": "string",
                                "enum": ["read", "write", "analyze", "summarize", "search", "organize"]
                            },
                            "path": {
                                "type": "string",
                                "description": "File or directory path"
                            },
                            "content": {
                                "type": "string",
                                "description": "Content for write operations"
                            },
                            "query": {
                                "type": "string",
                                "description": "Search query or analysis request"
                            },
                            "llm_assist": {
                                "type": "boolean",
                                "description": "Use LLM for intelligent processing",
                                "default": True
                            }
                        },
                        "required": ["operation", "path"]
                    }
                )


async def handle_file_manager(args: Dict[str, Any]):
    """Handle file operations with LLM assistance"""
    operation = args.get("operation")
    path = args.get("path")
    content = args.get("content", "")
    query = args.get("query", "")
    llm_assist = args.get("llm_assist", True)

    result = {}

    try:
        if operation == "read":
            with open(path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            result = {"content": file_content, "size": len(file_content)}

            if llm_assist and query:
                analysis = await simulate_llm_response(
                    f"Analyze this file content based on: {query}\n\nContent:\n{file_content[:2000]}...",
                    "llama-3.3-70b-versatile", 1000, 0.5
                )
                result["analysis"] = analysis

        elif operation == "write":
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            result = {"success": True, "bytes_written": len(content)}

        elif operation == "analyze":
            with open(path, 'r', encoding='utf-8') as f:
                file_content = f.read()

            if llm_assist:
                analysis_prompt = f"Provide a comprehensive analysis of this file:\n\n{file_content[:3000]}..."
                analysis = await simulate_llm_response(analysis_prompt, "llama-3.3-70b-versatile", 1500, 0.3)
                result = {"analysis": analysis, "file_size": len(file_content)}
            else:
                result = {"word_count": len(file_content.split()), "char_count": len(file_content)}

        elif operation == "summarize":
            with open(path, 'r', encoding='utf-8') as f:
                file_content = f.read()

            summary_prompt = f"Create a concise summary of this content:\n\n{file_content[:4000]}..."
            summary = await simulate_llm_response(summary_prompt, "llama-3.3-70b-versatile", 500, 0.3)
            result = {"summary": summary, "original_length": len(file_content)}

        await log_file_operation(operation, path, "success")

    except Exception as e:
        result = {"error": str(e)}
        await log_file_operation(operation, path, "error")

    # return CallToolResult(
    #     content=[TextContent(type="text", text=json.dumps(result, indent=2))]
    # )
    return [TextContent(type="text", text=json.dumps(result, indent=2))]