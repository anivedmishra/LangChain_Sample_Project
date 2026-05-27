# Story Writer Assignment — LangChain Single-Agent Project

This repository demonstrates the Story Writer agent built with LangChain and OpenAI.

The previous `Email Humanizer` content has been archived in `archive/`.

## Assignment Overview

Anived Mishra — Story Writer Agent

Use Case: A user provides a theme or a one-line story prompt. The agent first creates a story outline and then expands it into a complete short story.

Tools implemented:
- `create_story_outline(prompt)` — produce characters, setting, conflict, and resolution
- `write_short_story(outline)` — expand the outline into a 400–600 word short story

## Evaluation Criteria

| Criteria | Points |
|---|---:|
| Code follows the same LangChain agent structure as `email_humanizer.py` | 20 |
| Both tools are implemented correctly using `@tool` and `PromptTemplate` | 20 |
| Agent runs end-to-end without errors | 20 |
| `README.md` clearly explains the use case and how to run it | 20 |
| GitHub repo is public, clean, and has `.env.example` (no real API key committed) | 20 |
| **Total** | **100** |

## Setup

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

## Test script (automated check)

Run the included quick test which invokes the agent on a sample prompt and prints the output:

```bash
python run_story_test.py
```

This test script uses the same `.env` API key and will print a generated title + short story to stdout.

## Files of interest

- `story_writer_agent.py` — the agent implementation using LangChain's `@tool`, `PromptTemplate`, and `create_agent`.
- `run_story_test.py` — small test harness that runs the agent on a sample prompt.
- `.env.example` — placeholder for `OPENAI_API_KEY` (no real keys committed).
- `archive/` — contains backups of earlier README and archived examples (e.g., the original `email_humanizer.py` content).

## Notes for reviewers

- The repository now focuses on the Story Writer assignment; archived examples were moved to `archive/` to keep the main README and project scope aligned with the assignment.
- Confirm the repo is public on GitHub to satisfy the 'public, clean' criterion.

---

If you'd like I can also add the full assignment text verbatim into `README.md` or create a `assignment.md` file in the repo — tell me which you prefer and I'll commit it.

