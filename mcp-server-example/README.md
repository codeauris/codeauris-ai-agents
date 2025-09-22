
## Setup Python Virtual Environment

**Create virtual environment**
- python -m venv mcp-venv

**Activate on Linux/macOS**
- source mcp-venv/bin/activate

**Activate on Windows**
- mcp-venv\Scripts\activate

## Install Python Dependencies

**Make sure virtual environment is activated**
- source mcp-venv/bin/activate   # Linux/macOS
- mcp-venv\Scripts\activate      # Windows

**Install dependencies from requirements.txt**
- pip install -r requirements.txt

## Running the MCP Server with Inspector

**Install MCP Inspector globally using npm**
- npm install -g @modelcontextprotocol/inspector

**Start the MCP server and open Inspector**
- npx @modelcontextprotocol/inspector python mcp_app.py
