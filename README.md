# Story Writer Assignment — LangChain Single-Agent Project

## Setup What it does:

Turns a one-line story prompt into a structured outline, then expands it into a 400–600 word short story.

1. Clone the repository (or use your existing local copy):

```bash
git clone https://github.com/anivedmishra/Langchain_sample_project.git
cd Langchain_sample_project
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the env example and add your OpenAI key:

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY=sk-your-key-here
```

## Run the Story Writer Agent (interactive)

```bash
python story_writer_agent.py
```

Follow the prompt and enter a one-line story idea (e.g., "a robot who learns to feel emotions").


## Files of interest

- `story_writer_agent.py` — the agent implementation using LangChain's `@tool`, `PromptTemplate`, and `create_agent`.
- `.env.example` — placeholder for `OPENAI_API_KEY` (no real keys committed).
- `archive/` — contains backups of earlier README and archived examples (e.g., the original `email_humanizer.py` content).



