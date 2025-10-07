from typing import Dict
from mcp.types import Prompt

data_analysis_prompt = Prompt(
                    name="data_analysis",
                    description="AI-powered data analysis and insights",
                    arguments=[
                        {"name": "data", "description": "Data to analyze", "required": True},
                        {"name": "analysis_type", "description": "Type of analysis"},
                        {"name": "objectives", "description": "Analysis objectives"},
                        {"name": "output_format", "description": "Desired output format"}
                    ]
                )


async def generate_data_analysis_prompt(args: Dict[str, str]) -> str:
    data = args.get("data", "")
    analysis_type = args.get("analysis_type", "exploratory")
    objectives = args.get("objectives", "general insights")
    output_format = args.get("output_format", "detailed report")

    return f"""Please analyze the following data with an {analysis_type} approach:

Data:
{data}

Analysis Objectives: {objectives}
Desired Output Format: {output_format}

Please provide:
1. Data overview and structure assessment
2. Statistical summary and distributions
3. Pattern identification and trends
4. Correlation analysis
5. Outlier detection and analysis
6. Key insights and findings
7. Actionable recommendations
8. Visualization suggestions
9. Limitations and caveats
10. Next steps for further analysis"""