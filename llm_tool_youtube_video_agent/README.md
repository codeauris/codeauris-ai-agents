#  LLMs with Tools | CodeAuris
- Code example for LLM with Tools. We are creating a YouTube Video Transcript Agent for Customer Support.
- YouTube Video Transcript Agent for Customer Support

**Links:**
- [Video link](https://www.youtube.com/watch?v=X_iace1GOxs)
- [Blog link]()

**How to run this example**
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

