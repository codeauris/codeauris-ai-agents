#  MCP Server Example | CodeAuris
- Code example for creating a basic MCP server. We will demonstrate our MCP server using ModelContextProtocol Inspector.
- Connecting MCP server using ModelContextProtocol Inspector 

**Links:**
- [Video link]()
- [Blog link]()

**How to run this example**
- Clone this repo 
- Navigate to downloaded folder and create new virtual environment
```
python -m venv mcp-venv
```
**Activate virtual environment**
```
# mac/linux
source mcp-venv/bin/activate

# windows
mcp-venv\Scripts\activate
```

**Install dependencies**
```
pip install -r requirements.txt
```

**Install MCP Inspector globally using npm**
```
npm install -g @modelcontextprotocol/inspector
```

**Start the MCP server and open Inspector**
```
npx @modelcontextprotocol/inspector python mcp_app.py
```
