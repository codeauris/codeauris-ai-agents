from typing import Dict
from mcp.types import Prompt

research_assistant_prompt = Prompt(
                    name="research_assistant",
                    description="AI research assistant for comprehensive topic exploration",
                    arguments=[
                        {"name": "topic", "description": "Research topic", "required": True},
                        {"name": "depth", "description": "Research depth level"},
                        {"name": "perspective", "description": "Research perspective"},
                        {"name": "sources", "description": "Preferred source types"}
                    ]
                )


async def generate_research_prompt(args: Dict[str, str]) -> str:
    topic = args.get("topic", "")
    depth = args.get("depth", "comprehensive")
    perspective = args.get("perspective", "balanced")
    sources = args.get("sources", "academic and industry")

    return f"""Please conduct {depth} research on the topic: {topic}

Research Perspective: {perspective}
Preferred Sources: {sources}

Please provide:
1. Executive summary of the topic
2. Historical context and background
3. Current state of the field
4. Key stakeholders and perspectives
5. Recent developments and trends
6. Challenges and opportunities
7. Future outlook and predictions
8. Credible sources and references
9. Conflicting viewpoints (if any)
10. Recommendations for further research

Please ensure the research is thorough, balanced, and well-sourced."""