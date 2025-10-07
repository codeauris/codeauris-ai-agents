from typing import Dict
from mcp.types import Prompt

technical_writer_prompt = Prompt(
                    name="technical_writer",
                    description="AI technical writing assistant",
                    arguments=[
                        {"name": "content", "description": "Content to document", "required": True},
                        {"name": "audience", "description": "Target audience"},
                        {"name": "format", "description": "Documentation format"},
                        {"name": "style", "description": "Writing style"}
                    ]
                )


async def generate_technical_writing_prompt(args: Dict[str, str]) -> str:
    content = args.get("content", "")
    audience = args.get("audience", "technical professionals")
    format_type = args.get("format", "comprehensive documentation")
    style = args.get("style", "clear and professional")

    return f"""Please create {format_type} for the following content:

Content to Document:
{content}

Target Audience: {audience}
Writing Style: {style}

Please include:
1. Clear and concise overview
2. Detailed explanations with examples
3. Step-by-step procedures (if applicable)
4. Code samples or technical examples
5. Best practices and recommendations
6. Troubleshooting guide
7. FAQs or common issues
8. References and additional resources
9. Proper formatting and structure
10. Visual aids suggestions (diagrams, flowcharts)

Ensure the documentation is accessible to the target audience while maintaining technical accuracy."""