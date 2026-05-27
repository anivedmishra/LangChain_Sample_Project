# Story Writer Agent - LangChain Single Agent Project

A beginner-friendly project that generates **single agent** using **LangChain + OpenAI**. The agent creates short stories from a simple idea.

## What You'll Learn

- How LangChain works (LLMs, prompts, tools, agents)
- How to create tools using the `@tool` decorator
- How an agent decides which tools to call and in what order
- How `PromptTemplate` shapes LLM output
- How the agent's tool-calling loop works (think -> act -> observe -> repeat)

## How It Works

```text
User's story prompt
       |
       v
[Agent thinks: "I should create a story outline first"]
       |
       v
[Tool: create_story_outline]
Creates:
- Characters
- Setting
- Conflict
- Resolution
       |
       v
[Agent thinks: "Now I can expand this into a story"]
       |
       v
[Tool: write_short_story]
Generates a complete short story
       |
       v
Final story returned to user

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Setup

### 1. Clone the repository

```bash
git clone git clone https://github.com/anivedmishra/LangChain_Sample_Project_1.git
cd Langchain_sample_project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example env file and add your real key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Run

```bash
python story_writer.py
```

You'll see an interactive prompt:

```
============================================================
  Story Writer Agent
  Powered by LangChain + OpenAI
============================================================

Describe the story theme or give one line prompt and the agent will
create a creative story for you.

Type 'quit' to exit.

Your story idea:
```

Type your story idea (e.g., `Write a story about characters during the Mughal Empire`) and the agent will generate a creative story.. You'll also see detailed logs showing the agent's reasoning and tool calls.

## Example

**Input:**
```
A story about 3 friends who have a fight but then they realize how important friendship is.
```

**Output:**
```
Tides of Truth

The salty breeze tangled Mia’s dark curls as she sat on the weathered bench overlooking the restless sea. Her sketchbook lay forgotten on her lap, lines half-drawn and abandoned. The summer sun dipped low, casting long shadows over the small coastal town that had been their sanctuary for years.

She hadn’t spoken to Liam or Zoe in days—not since the argument that shattered their carefree summer.

It had started so innocently. The three of them—Mia, Liam, and Zoe—had been working on a mural for the town’s annual festival, a project meant to celebrate their friendship and their shared love for this sun-kissed place. Mia, with her fiery passion and brush in hand, was eager to pour her heart into every stroke. Liam, practical and sharp, had taken charge of logistics, making sure paint was ordered, schedules set. Zoe, ever the peacemaker, had tried to balance their differing ideas with a cheerful smile.

But then a miscommunication spiraled out of control.

“I thought you said you’d handle the paint colors, Liam,” Mia had snapped, her voice trembling with frustration. “You went behind my back and changed the palette without telling me.”

Liam’s jaw tightened. “I did what was best for the project. You were being stubborn about the colors—no offense—but we needed something that would last.”

Zoe stepped between them, hands raised. “Guys, please, let’s not do this now.”

But the damage was done. Harsh words flew like jagged shells, and by the end of the afternoon, their friendship lay fractured like driftwood scattered on the shore.

Now, as Mia watched the waves crash in rhythm, she felt the ache of silence more keenly than the ocean’s roar.

Footsteps approached, light and hesitant. “Mia?”

She looked up to see Zoe, her bright eyes shadowed with worry but her smile gentle.

“I’ve missed this,” Zoe said softly, settling beside her. “The three of us.”

Mia nodded, biting her lip. “I miss us too. But Liam... he’s still angry. I don’t even know if he wants to talk.”

Zoe shook her head. “He’s hurting, just like you. I think we all got caught up in trying to be right instead of listening.”

Before Mia could respond, Liam appeared at the edge of the path, hands shoved deep in his pockets, his usual witty spark dimmed.

“I wasn’t sure if you’d come,” Liam admitted, stepping closer.

Mia met his gaze, the tension between them thick as fog. “I’m sorry, Liam. I should have trusted you more, and... I should have said how I felt instead of shutting down.”

Liam’s lips twitched into a tentative smile. “And I should’ve been more honest about why I changed the colors. I was scared the mural wouldn’t come together, and instead of telling you, I just made the call.”

Zoe reached out, taking both their hands. “We’re stronger when we’re honest with each other. And when we forgive.”

The three of them stood together, the sun slipping beneath the horizon, painting the sky in hues of orange and pink—much like the mural they’d yet to finish.

Mia pulled her sketchbook from her bag. “How about we start fresh? Together.”

Liam chuckled, the sound light and freeing. “As long as I get veto power on the neon pink.”

Zoe laughed, the sound mingling with the waves. “Deal.”

The night wrapped around them like a warm blanket, and in that moment, the tides of misunderstanding gave way to the currents of truth and friendship—unbreakable, like the steady sea.
```

## Project Structure

```
.
├── story_writer.py   # Main agent code (fully commented)
├── requirements.txt     # Python dependencies
├── .env.example         # API key template
├── .gitignore           # Keeps secrets and venv out of git
└── README.md            # This file
├── Archive         # Old Files that I used for repo
└── .venv            # Virtual File that was created.
```

## Tech Stack

- [LangChain](https://python.langchain.com/) - Framework for building LLM applications
- [OpenAI GPT-4o-mini](https://platform.openai.com/) - The LLM powering the agent
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
