#  LLMs with Tools - YouTube Video Transcript Agent for Customer Support | Kodex Academy
Code example in AI agents series. Here I use Groq LLM.

**Links:**
- [Video link](https://www.youtube.com/watch?v=X_iace1GOxs)
- [Blog link]()

## How to run this example

1. Clone this repo
2. Navigate to downloaded folder and create new venv
```
python -m venv llm-venv
```
3. Activate venv
```
# mac/linux
source llm-venv/bin/activate

# windows
llm-venv\Scripts\activate
```
4. Environment variables
Create .env file for environment variables. Add following variables
- GROQ_API_KEY=<GROQ_API_KEY>
- GROQ_LLM_MODEL=llama-3.3-70b-versatile

5. Install dependencies
```
pip install -r requirements.txt
```

6. Run script
```
python youtube_video_agent_context_tool.py
```

