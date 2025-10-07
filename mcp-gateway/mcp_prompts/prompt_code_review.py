from typing import Dict
from mcp.types import Prompt

code_review_prompt = Prompt(
                    name="code_review",
                    description="Comprehensive code review with AI insights",
                    arguments=[
                        {"name": "code", "description": "Code to review", "required": True},
                        {"name": "language", "description": "Programming language"},
                        {"name": "focus", "description": "Review focus areas"},
                        {"name": "style_guide", "description": "Style guide to follow"}
                    ]
                )


async def generate_code_review_prompt(args: Dict[str, str]) -> str:
    code = args.get("code", "")
    language = args.get("language", "unknown")
    focus = args.get("focus", "general code quality")
    style_guide = args.get("style_guide", "industry standards")

    return f"""Please conduct a comprehensive code review for the following {language} code:

```{language}
{code}
```

Review Focus: {focus}
Style Guide: {style_guide}

Please provide detailed feedback on:
1. Code correctness and logic
2. Performance optimization opportunities  
3. Security vulnerabilities
4. Code maintainability and readability
5. Adherence to best practices and style guidelines
6. Test coverage recommendations
7. Documentation quality
8. Specific improvement suggestions with examples

Please be thorough and constructive in your review."""