# MCP Server Example | CodeAuris

A Model Context Protocol (MCP) server implementation example from CodeAuris, providing AI-powered tools, resources, and prompts for intelligent automation and custom software solutions.

## Overview

This MCP server exposes capabilities through a standardized interface that can be integrated with AI assistants and applications. It includes tools for querying company information, sending newsletters, and managing resources.

**Links:**
- [Video link]()

## Features

### 🎯 Prompts
- **user_greeting**: Personalized greeting prompt for welcoming users to CodeAuris

### 📚 Resources
- **codeauris_details**: Text resource containing comprehensive information about CodeAuris services, offerings, and expertise

### 🛠️ Tools
- **codeauris_chat**: Query the CodeAuris knowledge base with case-insensitive search
- **send_email**: Send newsletter emails to recipients using SMTP

## Project Structure

```
.
├── mcp_app.py           # Main application entry point
├── mcp_instance.py      # MCP instance initialization
├── mcp_prompt.py        # Prompt definitions
├── mcp_resource.py      # Resource loaders
├── mcp_tool.py          # Tool implementations
├── requirements.txt     # Python dependencies
├── resources/
│   ├── codeauris.txt    # Company information knowledge base
│   └── email_template.txt # Newsletter email template
└── .env                 # Environment variables (not included)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/codeauris/codeauris-ai-agents.git
cd codeauris-ai-agents/mcp-server-example
```

2. **Activate virtual environment & Install dependencies**
```
python -m venv mcp-venv
```
```
# mac/linux
source mcp-venv/bin/activate

# windows
mcp-venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Create a `.env` file in the project root:
```env
SENDER_EMAIL=your-email@gmail.com
SENDER_EMAIL_PASSWORD=your-app-password
```

> **Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

4. **Prepare resources**

Ensure the following files exist in the `resources/` directory:
- `codeauris.txt` - Company information
- `email_template.txt` - Email template for newsletters

## Usage

### Running the Server

Start the MCP server with stdio transport:

```bash
python mcp_app.py
```

The server will listen for MCP protocol messages on stdin/stdout.

### Available Operations

#### 1. User Greeting Prompt
```python
# Returns a personalized greeting
# Default: "Hello, Learner! Welcome to CodeAuris."
# With name: "Hello, John! Welcome to CodeAuris."
```

#### 2. Query CodeAuris Knowledge Base
```python
# Tool: codeauris_chat
# Query the knowledge base for specific information
# Returns matching lines containing the query term
```

#### 3. Send Newsletter Email
```python
# Tool: send_email
# Parameters:
#   - subject: Email subject line
#   - recipient: Recipient email address
#   - smtp_server: SMTP server (default: smtp.gmail.com)
#   - smtp_port: SMTP port (default: 587)
```

## API Reference

### Prompts

#### `user_greeting(name: str = "Learner")`
Returns a greeting message for the specified user.

**Parameters:**
- `name` (str, optional): User's name. Default: "Learner"

**Returns:** Formatted greeting string

### Resources

#### `load_codeauris_details()`
Loads CodeAuris company information from the resources directory.

**URI:** `http://localhost/codeauris`

**Returns:** Text content of codeauris.txt

### Tools

#### `codeauris_chat(query: str)`
Searches the CodeAuris knowledge base for matching content.

**Parameters:**
- `query` (str): Search term (case-insensitive)

**Returns:**
```json
{
  "query": "search term",
  "matches": ["matching line 1", "matching line 2"],
  "count": 2
}
```

#### `send_email(subject: str, recipient: str, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587)`
Sends a newsletter email using the configured template.

**Parameters:**
- `subject` (str): Email subject
- `recipient` (str): Recipient email address
- `smtp_server` (str, optional): SMTP server address
- `smtp_port` (int, optional): SMTP server port

**Returns:** Boolean indicating success/failure

## Configuration

### Email Configuration

The email tool uses SMTP with TLS encryption. Configure the following environment variables:

- `SENDER_EMAIL`: Sender email address
- `SENDER_EMAIL_PASSWORD`: Email account password or app-specific password

### Customizing Resources

**CodeAuris Information (`resources/codeauris.txt`)**
Update this file to reflect current company offerings, services, and information.

**Email Template (`resources/email_template.txt`)**
Customize the newsletter template with your own content. Supports HTML formatting.

## About CodeAuris

CodeAuris specializes in:
- AI Software Development
- Custom Software Engineering
- Cloud & DevOps Solutions
- Software Consulting
- Full Product Lifecycle Support

Visit [CodeAuris.com](https://codeauris.com) for more information.

## Development

### Adding New Tools

1. Define the tool in `mcp_tool.py`:
```python
@mcp.tool("tool_name")
async def tool_name(param: str):
    """Tool description"""
    # Implementation
    return result
```

2. Import in `mcp_app.py` if using a separate module

### Adding New Resources

1. Define the resource in `mcp_resource.py`:
```python
@mcp.resource("http://localhost/resource_name")
def load_resource() -> str:
    """Resource description"""
    # Load and return resource
    return content
```

### Adding New Prompts

1. Define the prompt in `mcp_prompt.py`:
```python
@mcp.prompt("prompt_name")
def prompt_name(param: str = "default"):
    """Prompt description"""
    return f"Prompt content with {param}"
```

## Security Considerations

- Never commit `.env` file with sensitive credentials
- Use app-specific passwords for email services
- Implement rate limiting for production deployments
- Validate all user inputs in tools
- Use secure SMTP connections (TLS/SSL)

## Troubleshooting

### Email Sending Issues
- Verify SMTP credentials in `.env` file
- Check firewall settings for port 587
- Enable "Less secure app access" or use App Passwords for Gmail
- Verify recipient email addresses

### Resource Loading Issues
- Ensure `resources/` directory exists
- Check file permissions for reading
- Verify file encoding is UTF-8

## License

MIT License - see LICENSE file for details

## Author

**CodeAuris**
- Email: codeauris@gmail.com
- GitHub: [@codeauris](https://github.com/codeauris)
