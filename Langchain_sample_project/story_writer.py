"""
===========================================================================
 Story Writer -- A Beginner's LangChain Single-Agent Project
===========================================================================

 WHAT THIS PROJECT TEACHES YOU:
   1. How LangChain works (chains, prompts, LLMs, tools, agents)
   2. How to build a SINGLE AGENT that uses tools
   3. How to connect LangChain to OpenAI
   4. How prompt templates shape LLM output
   5. How an agent "thinks" using a tool-calling loop

 HOW LANGCHAIN WORKS (the big picture):
   LangChain is a framework that makes it easy to build LLM-powered apps.

     [User Input] --> [Prompt Template] --> [LLM (GPT)] --> [Output]

   - Prompt Template : A reusable template with placeholders (like a form)
   - LLM            : The AI model that generates text (OpenAI GPT)
   - Output         : The generated response

 WHAT IS AN AGENT?
   An agent is an LLM that can USE TOOLS and DECIDE what to do next.
   Unlike a simple chain (input -> LLM -> output), an agent can:
     1. Think about what it needs to do
     2. Pick a tool to use
     3. Use the tool and see the result
     4. Decide if it needs more steps or if it's done

   This is the tool-calling loop:
     THINK -> ACT -> OBSERVE -> THINK -> ... -> FINAL ANSWER

 HOW THIS PROJECT FLOWS:
   1. User provides an email idea (e.g., "thank my team for Q4 results")
   2. Agent calls draft_email tool   -> creates a formal email draft
   3. Agent calls humanize_email tool -> rewrites it to sound natural
   4. Agent returns the final humanized email to the user

 KEY LANGCHAIN COMPONENTS USED:
   - ChatOpenAI      : LLM wrapper that sends prompts to OpenAI's GPT API
   - PromptTemplate  : Template with {placeholders} filled before sending to LLM
   - @tool decorator : Turns a Python function into a tool the agent can call
   - create_agent    : Wires LLM + tools + system prompt into a runnable agent

 SETUP:
   1. pip install -r requirements.txt
   2. Copy .env.example to .env and add your OpenAI API key
   3. python story_writer.py

 See langchain_tutorial.md for a full beginner's guide to LangChain.
 See architecture_diagram.drawio for a visual diagram of this project.
===========================================================================
"""

import logging
import sys
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("StoryWriter")

logger.info("Starting Story Writer Agent...")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key.startswith("sk-your"):
    logger.error("OPENAI_API_KEY not set! Copy .env.example to .env and add your key.")
    sys.exit(1)

logger.info("API key loaded successfully")
logger.info("All LangChain components imported")
logger.info("Initializing the LLM (OpenAI GPT)...")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7,
    verbose=True,
)

logger.info("LLM initialized: model=gpt-4.1-mini, temperature=0.7")
logger.info("Defining agent tools...")


@tool
def create_story_outline(prompt: str) -> str:
    """
    Generate a structured story outline from a theme or one line prompt
    Use this tool FIRST when the user provides a story idea.
    Input should be the user's story theme or one line prompt.
    Returns a detailed outline with characters, setting, conflict and resolution.
    """
    logger.info(f"[Tool: create_story_outline] Received idea: '{prompt}'")

    outline_prompt = PromptTemplate(
        input_variables=["prompt"],
        template="""You are a creative fiction planner.
Given the following istory idea, create a detailed story outline.

 Story Idea: {prompt}

Structure your outline with these clearly labelled sections:
**Chracters**
-List 2-3 main characters with a one line description of each.
**Setting**
-Describe the time and place where the story happens.
**Conflict**
-What is the main problem or challenge the characters face?
**Resolution**
-How does the story end? What is the solution to the conflict? What does the characters learn or how do they change?
-
Return ONLY the outline, nothing else.""",
    )

    formatted_prompt = outline_prompt.format(prompt=prompt)
    logger.info("[Tool: create_story_outline] Sending prompt to LLM...")

    response = llm.invoke(formatted_prompt)

    logger.info("[Tool: create_story_outline] Outline created successfully!")
    return response.content


@tool
def write_short_story(outline: str) -> str:
    """
    Takes a story outline and expands it into a short story with Title
    Use this tool AFTER create_story_outline to develop the full story.
    Input should be the full story outline generated by the first tool.
    Returns a short story with a title. (400-600 words) with a title.
    """
    logger.info("[Tool: write_short_story] Expanding outline into full story...")

    story_prompt = PromptTemplate(
        input_variables=["outline"],
        template="""You are a skilled fiction author who writes engaging short stories.

Using the story outline velow, write a complete short story with a title. Make it creative, engaging, and well-written.

Rules:
- Give the story a compelling title that captures the essence of the story.
- write between 400-600 words.
- Use vivid descriptions and dialogue to bring the characters and setting to life.
- Have a hook in the beginning to grab the reader's attention, a clear conflict, and a satisfying resolution.
- End with satisfying conclusion that ties back to the story's theme.
- The story should be tied together and flow well, not just a list of events from the outline.


Story outline:
{outline}

Return ONLY the short story, nothing else.""",
    )

    formatted_prompt = story_prompt.format(outline=outline)
    logger.info("[Tool: write_short_story] Sending to LLM for story generation...")

    response = llm.invoke(formatted_prompt)

    logger.info("[Tool: write_short_story] Short story generated successfully!")
    return response.content


tools = [create_story_outline, write_short_story]
logger.info(f"Tools registered: {[t.name for t in tools]}")
logger.info("Creating the agent...")

SYSTEM_PROMPT = """You are a Story Writer assistant. Your job is to help users
create engaging short stories.

When the user gives you a story idea, follow these steps:
1. First, use the create_story_outline tool to create a structured story outline.
2. Then, use the write_short_story tool to expand the outline into a full story.
3. Return the final short story to the user and should be less than 600 words.

Always use both tools in order: outline first, then write."""

agent_graph = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    debug=True,
)

logger.info("Agent created and ready to run!")


def run_story_writer(story_prompt: str) -> str:
    """
    Main function to run the story writer agent.

    Args:
        story_prompt: A brief description of the story you want to write.
                    Example: "thank my team for hitting Q4 targets"

    Returns:
        A humanized, natural-sounding email.
    """
    logger.info("=" * 60)
    logger.info(f"USER'S STORY IDEA: {story_prompt}")
    logger.info("=" * 60)
    logger.info("Agent is now thinking... watch the tool-calling loop below!")
    logger.info("-" * 60)

    result = agent_graph.invoke(
        {"messages": [HumanMessage(content=story_prompt)]}
    )

    final_story = result["messages"][-1].content

    logger.info("-" * 60)
    logger.info("Agent finished! Here's your short story:")
    logger.info("=" * 60)

    return final_story


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  STORY WRITER AGENT")
    print("  Powered by LangChain + OpenAI")
    print("=" * 60)
    print("\nDescribe the story you want to write, and the agent will")
    print("create an engaging short story for you.\n")
    print("Type 'quit' to exit.\n")

    while True:
        story_prompt = input("Your story prompt: ").strip()

        if not story_prompt:
            print("Please enter a story prompt.\n")
            continue

        if story_prompt.lower() in ("quit", "exit", "q"):
            print("\nGoodbye! Happy writing!")
            break

        try:
            final_story = run_story_writer(story_prompt)

            print("\n" + "=" * 60)
            print("YOUR SHORT STORY:")
            print("=" * 60)
            print(final_story)
            print("=" * 60 + "\n")

        except Exception as e:
            logger.error(f"Something went wrong: {e}")
            print(f"\nError: {e}")
            print("Please check your API key and try again.\n")
