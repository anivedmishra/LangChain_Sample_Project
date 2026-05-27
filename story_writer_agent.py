"""
=============================================
 STORY WRITER AGENT — LangChain Single-Agent
=============================================

This agent turns a one-line story prompt into a short story.

Tools:
- `create_story_outline(prompt)` — produce characters, setting, conflict, resolution
- `write_short_story(outline)`   — expand the outline into a 400-600 word story

Run:
    python story_writer_agent.py

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

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7, verbose=True)


@tool
def create_story_outline(prompt: str) -> str:
    """
    Generate a structured story outline from a theme or one-line prompt.
    Returns a bullet-point outline describing characters, setting, conflict, and resolution.
    """
    logger.info(f"[Tool: create_story_outline] Prompt: {prompt}")

    outline_template = PromptTemplate(
        input_variables=["prompt"],
        template=(
            "You are a professional fiction writer. Given a short prompt, produce a detailed story outline.\n"
            "Include: main characters (names + short descriptions), setting, central conflict, major plot beats, and a concise resolution.\n\n"
            "Prompt: {prompt}\n\n"
            "Return the outline as bullet points, grouped under headings: Characters, Setting, Conflict, Plot Beats, Resolution."
        ),
    )

    formatted = outline_template.format(prompt=prompt)
    response = llm.invoke(formatted)
    logger.info("[Tool: create_story_outline] Outline generated")
    return response.content


@tool
def write_short_story(outline: str) -> str:
    """
    Expand a story outline into a 400-600 word short story with a title.
    Input: the outline produced by create_story_outline.
    Output: a polished short story (title + body).
    """
    logger.info("[Tool: write_short_story] Expanding outline into story")

    story_template = PromptTemplate(
        input_variables=["outline"],
        template=(
            "You are a skilled short story writer. Use the following outline to write a compelling short story (400-600 words).\n"
            "Keep prose clear, engaging, and emotionally resonant. Provide a short title on the first line, then a blank line, then the story.\n\n"
            "Outline:\n{outline}\n\n"
            "Return ONLY the title and story, nothing else."
        ),
    )

    formatted = story_template.format(outline=outline)
    response = llm.invoke(formatted)
    logger.info("[Tool: write_short_story] Story written")
    return response.content


tools = [create_story_outline, write_short_story]
logger.info(f"Tools registered: {[t.name for t in tools]}")

SYSTEM_PROMPT = """You are a Story Writer assistant. When the user gives a prompt, first call
create_story_outline to produce a structured outline, then call write_short_story to expand it
into a 400-600 word short story. Always use both tools in that order."""

agent = create_agent(model=llm, tools=tools, system_prompt=SYSTEM_PROMPT, debug=True)


def run_story_writer(prompt: str) -> str:
    logger.info("=" * 60)
    logger.info(f"USER PROMPT: {prompt}")
    logger.info("Agent is thinking and will call tools in sequence...")

    result = agent.invoke({"messages": [HumanMessage(content=prompt)]})
    final = result["messages"][-1].content

    logger.info("Agent finished writing the story")
    return final


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  STORY WRITER AGENT")
    print("  Powered by LangChain + OpenAI")
    print("=" * 60)
    print("\nProvide a short theme or one-line story prompt. Type 'quit' to exit.\n")

    while True:
        prompt = input("Your story prompt: ").strip()
        if not prompt:
            print("Please enter a prompt.\n")
            continue
        if prompt.lower() in ("quit", "exit", "q"):
            print("\nGoodbye!")
            break

        try:
            story = run_story_writer(prompt)
            print("\n" + "=" * 60)
            print("YOUR SHORT STORY:")
            print("=" * 60)
            print(story)
            print("\n" + "=" * 60 + "\n")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}\nCheck your API key and try again.")
