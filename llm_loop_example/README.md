#  LLMs in Loop | CodeAuris
- Code example for LLM in Loop. We are creating a Self evaluating loop for Document Correction.
- Document Correction Loop 

**Links:**
- [Video link](https://www.youtube.com/watch?v=Xtv3ebMMG0g)

**Details**
- Read the resource text content given in the `resource` folder. Text file name is hardcoded in code. Change it according to your use.
- This code will correct the given document and will store the corrected document at each stage in `corrected_files` folder
- correction_agent.py - This script act as a correction agent. It uses Groq LLM to correct the given document. Also, stores the corrected document in `corrected_files` folder.
- evaluation_agent.py - This script act as a evaluation agent. It uses Groq LLM to evaluate the corrected document.
- This is an example of Self-Correcting LLM in Loop.

## How to run this example
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
