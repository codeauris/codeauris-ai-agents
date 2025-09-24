#  LLMs with Tools | CodeAuris
- Code example for LLM with Tools. We are creating a YouTube Video Transcript Agent for Customer Support.
- YouTube Video Transcript Agent for Customer Support

**Links:**
- [Video link](https://www.youtube.com/watch?v=pEy4m8lzZss)

**Details**
- This code will extract the English transcript from any given YouTube video URL
- We can then provide the query, to get results based on the extracted content
- youtube_video_agent_context_tool.py - stores the conversation history and responses including your previous chat
- youtube_video_agent_stateless_tool.py - does not store the conversation history

## How to run this example
- Clone this repo 
- Navigate to downloaded folder and create new venv
```
python -m venv llm-venv
```
**Activate virtual environment**
```
# mac/linux
source llm-venv/bin/activate

# windows
llm-venv\Scripts\activate
```
**Environment variables**
- Create .env file for environment variables. Add following variables
```
GROQ_API_KEY=<GROQ_API_KEY>
GROQ_LLM_MODEL=llama-3.3-70b-versatile
```

**Install dependencies**
```
pip install -r requirements.txt
```

**Run script**
```
python youtube_video_agent_context_tool.py
```
