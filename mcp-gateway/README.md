# MCP Gateway

A comprehensive Model Context Protocol (MCP) Gateway implementation that provides a unified interface for AI agents to interact with various tools, resources, and prompts. This gateway supports multiple LLM providers and includes database persistence for conversation history and analytics.

## 🌟 Features

- **Multi-LLM Support**: Integrates with Groq, OpenAI, Anthropic Claude, and Google Gemini
- **MCP Protocol Compliance**: Full implementation of the Model Context Protocol standard
- **5 Specialized Tools**: LLM query, file management, code assistance, data processing, and web research
- **4 Resource Types**: Conversations, documents, system status, and analytics
- **4 Prompt Templates**: Code review, data analysis, technical writing, and research assistance
- **SQLite Database**: Persistent storage for conversations, documents, and file operations
- **Async Architecture**: Built with asyncio for high-performance concurrent operations
- **Stdio Transport**: Standard MCP communication via stdin/stdout

## 📋 Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Available Tools](#available-tools)
- [Available Resources](#available-resources)
- [Available Prompts](#available-prompts)
- [Database Schema](#database-schema)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      MCP Gateway Server                     │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              mcp_gateway.py (Main Entry)               │ │
│  └─────────────────────┬──────────────────────────────────┘ │
│                        │                                    │
│  ┌─────────────────────▼──────────────────────────────────┐ │
│  │           mcp_handlers.py (Handler Registry)           │ │
│  └──────┬────────────────┬─────────────────┬──────────────┘ │
│         │                │                 │                │
│    ┌────▼─────┐    ┌────▼─────┐    ┌─────▼──────┐           │
│    │  Tools   │    │Resources │    │  Prompts   │           │
│    └────┬─────┘    └────┬─────┘    └─────┬──────┘           │
│         │               │                │                  │
└─────────┼───────────────┼────────────────┼───────────────── ┘
          │               │                │
     ┌────▼────┐    ┌─────▼──────┐   ┌─────▼──────┐
     │LLM Query│    │Conversation│   │Code Review │
     │File Mgr │    │Documents   │   │Data Analyst│
     │Code Asst│    │Analytics   │   │Tech Writer │
     │Data Proc│    │System Info │   │Researcher  │
     │Web Rsrch│    └────────────┘   └────────────┘
     └────┬────┘
          │
     ┌────▼─────────────────────────┐
     │  llm_call_methods.py         │
     │  (LLM Provider Abstraction)  │
     └────┬─────────────────────────┘
          │
     ┌────▼──────────────────────────┐
     │ Groq │ OpenAI │ Claude │ Gemini│
     └───────────────────────────────┘

     ┌─────────────────────────────┐
     │  database_operations.py     │
     │  (SQLite Persistence)       │
     └─────────────────────────────┘
```

## Prerequisites

- **Python**: >= 3.7 (recommended: 3.10+)
- **pip**: Latest version
- **SQLite3**: Included with Python
- **API Keys**: At least one LLM provider API key (Groq, OpenAI, Anthropic, or Google)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/codeauris/codeauris-ai-agents.git
cd codeauris-ai-agents/mcp-gateway
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# install in development mode
pip install -e .
```

## Configuration

### 1. Environment Variables

Create a `.env` file in the root directory:

```env
# LLM Configuration
LLM_TYPE=Groq
# Options: Groq, OpenAI, Anthropic, Gemini, or leave empty for simulation mode

# API Keys (add the one you're using)
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

# Database Configuration
DB_FOLDER=../data
DB_FOLDER_PATH=../data/mcp_gateway.db
```

### 2. Supported LLM Providers

| Provider | Status | Model Example |
|----------|--------|---------------|
| **Groq** | ✅ Implemented | `llama-3.1-70b-versatile` |
| **OpenAI** | 🔄 Ready (commented) | `gpt-4` |
| **Anthropic** | 🔄 Ready (commented) | `claude-3-sonnet-20240229` |
| **Gemini** | 🔄 Ready (commented) | `gemini-pro` |
| **Simulation** | ✅ Default fallback | N/A |

To enable additional providers, uncomment the relevant code in `llm_call_methods.py`.

## Usage

### Starting the MCP Gateway Server

```bash
# Make sure your virtual environment is activated
python mcp_gateway.py
```

The server will:
1. Load environment variables from `.env`
2. Initialize the SQLite database
3. Register all tools, resources, and prompts
4. Start listening on stdio for MCP protocol messages

### Connecting to the Gateway

The MCP Gateway uses the stdio transport protocol. Connect your MCP client application to communicate with the gateway:

```python
# Example: Connecting from an MCP client
from mcp.client import Client

async def connect_to_gateway():
    client = Client()
    await client.connect_stdio(["python", "mcp_gateway.py"])
    
    # List available tools
    tools = await client.list_tools()
    print("Available tools:", tools)
    
    # Call a tool
    result = await client.call_tool("llm_query", {
        "prompt": "What is the capital of France?",
        "model": "llama-3.1-70b-versatile",
        "max_tokens": 500,
        "temperature": 0.7
    })
```

## Available Tools

### 1. LLM Query (`llm_query`)
Query various LLM providers with custom parameters.

**Arguments:**
- `prompt` (string): The query text
- `model` (string): Model identifier (e.g., `llama-3.1-70b-versatile`)
- `max_tokens` (integer): Maximum response tokens
- `temperature` (float): Creativity level (0.0-1.0)

### 2. File Manager (`file_manager`)
Manage files and directories with various operations.

**Arguments:**
- `operation` (string): Operation type (read, write, delete, list, etc.)
- `path` (string): File or directory path
- `content` (string, optional): Content for write operations

### 3. Code Assistant (`code_assistant`)
Assist with code analysis, generation, and debugging.

**Arguments:**
- `action` (string): Action type (analyze, generate, debug, refactor)
- `code` (string): Source code to process
- `language` (string): Programming language

### 4. Data Processor (`data_processor`)
Process and analyze various data formats.

**Arguments:**
- `operation` (string): Processing operation (parse, transform, analyze)
- `data` (string): Input data
- `format` (string): Data format (json, csv, xml, etc.)

### 5. Web Researcher (`web_researcher`)
Research and gather information from web sources.

**Arguments:**
- `query` (string): Search query
- `sources` (array): Preferred sources
- `depth` (string): Research depth (quick, standard, comprehensive)

## Available Resources

### 1. Conversations (`mcp://gateway/conversations`)
Access conversation history and context.

**Returns:**
- Conversation ID
- Timestamp
- Context
- Response
- Model used
- Tokens consumed

### 2. Documents (`mcp://gateway/documents`)
Access stored documents and their metadata.

**Returns:**
- Document ID
- Title
- Content
- Tags
- Creation and update timestamps

### 3. System Status (`mcp://gateway/system`)
Get system health and performance metrics.

**Returns:**
- System uptime
- Resource usage
- Active connections
- Error rates

### 4. Analytics (`mcp://gateway/analytics`)
Access usage analytics and statistics.

**Returns:**
- Tool usage statistics
- Token consumption
- Response times
- Error logs

## Available Prompts

### 1. Code Review (`code_review`)
Generate comprehensive code review prompts.

**Arguments:**
- `code` (string): Code to review
- `language` (string): Programming language
- `focus_areas` (array, optional): Specific areas to focus on

### 2. Data Analysis (`data_analysis`)
Generate data analysis prompts.

**Arguments:**
- `data_description` (string): Description of the dataset
- `analysis_goals` (array): Analysis objectives
- `format` (string): Data format

### 3. Technical Writer (`technical_writer`)
Generate technical documentation prompts.

**Arguments:**
- `topic` (string): Documentation topic
- `audience` (string): Target audience
- `format` (string): Documentation format

### 4. Research Assistant (`research_assistant`)
Generate research and investigation prompts.

**Arguments:**
- `topic` (string): Research topic
- `scope` (string): Research scope
- `sources` (array, optional): Preferred sources

## Database Schema

The gateway uses SQLite with three main tables:

### Conversations Table
```sql
CREATE TABLE conversations (
    id TEXT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    context TEXT,
    response TEXT,
    model TEXT,
    tokens_used INTEGER
)
```

### Documents Table
```sql
CREATE TABLE documents (
    id TEXT PRIMARY KEY,
    title TEXT,
    content TEXT,
    tags TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

### File Operations Table
```sql
CREATE TABLE file_operations (
    id TEXT PRIMARY KEY,
    operation TEXT,
    file_path TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

## Development

### Project Structure

```
mcp-gateway/
├── mcp_gateway.py              # Main server entry point
├── mcp_handlers.py             # Handler registration
├── llm_call_methods.py         # LLM provider integrations
├── database_operations.py      # Database operations
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project metadata
├── .env                       # Environment variables (create this)
├── mcp_tools/                 # Tool implementations
│   ├── tool_llm_query.py
│   ├── tool_file_manager.py
│   ├── tool_code_assistant.py
│   ├── tool_data_processor.py
│   └── tool_web_researcher.py
├── mcp_resources/             # Resource implementations
│   ├── resource_conversation.py
│   ├── resource_document.py
│   ├── resource_system.py
│   └── resource_analytics.py
└── mcp_prompts/               # Prompt templates
    ├── prompt_code_review.py
    ├── prompt_data_analysis.py
    ├── prompt_technical_writer.py
    └── prompt_research_assistant.py
```

### Adding a New Tool

1. Create a new file in `mcp_tools/` (e.g., `tool_my_feature.py`)
2. Define the tool schema and handler function
3. Register the tool in `mcp_handlers.py`:

```python
# In list_tools()
tool_my_feature.my_feature_tool,

# In call_tool()
elif name == "my_feature":
    return await tool_my_feature.handle_my_feature(arguments)
```

### Adding a New LLM Provider

Uncomment and configure the relevant provider in `llm_call_methods.py`:

```python
# 1. Install the SDK
pip install openai  # or anthropic, google-generativeai, etc.

# 2. Add API key to .env
OPENAI_API_KEY=your_key_here

# 3. Uncomment the provider function in llm_call_methods.py

# 4. Update the simulate_llm_response() router
```

## Troubleshooting

### Common Issues

**Issue: Database not found**
```bash
# Solution: Check DB_FOLDER_PATH in .env
DB_FOLDER=../database
DB_FOLDER_PATH=../database/mcp_gateway.db
```

**Issue: LLM API errors**
```bash
# Solution: Verify API key and LLM_TYPE setting
LLM_TYPE=Groq
GROQ_API_KEY=your_actual_key_here
```

**Issue: Module not found**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

## License

MIT License - see LICENSE file for details

## Author

**CodeAuris**
- Email: codeauris@gmail.com
- GitHub: [@codeauris](https://github.com/codeauris)
