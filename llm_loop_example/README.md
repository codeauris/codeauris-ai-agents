#  LLMs in Loop | CodeAuris
- Code example for LLM in Loop. We are creating a Self evaluating loop for Document Correction.
- Document Correction Loop 

**Links:**
- [Video link]()
- [Blog link]()

**How to run this example**
- Clone this repo 
- Navigate to downloaded folder and create new virtual environment
```
python -m venv llm-loop
```
**Activate virtual environment**
```
# mac/linux
source llm-loop/bin/activate

# windows
llm-loop\Scripts\activate
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
python llm_loop_agent.py
```
