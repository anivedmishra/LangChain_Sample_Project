"""
run_story_test.py

Quick test harness that runs the Story Writer agent on a sample prompt
and prints the generated story. Requires `.env` with a valid `OPENAI_API_KEY`.
"""

from story_writer_agent import run_story_writer


def main():
    prompt = "a robot who learns to feel emotions"
    print("Running Story Writer agent test with prompt:\n", prompt)
    story = run_story_writer(prompt)
    print("\n--- Generated Story ---\n")
    print(story)


if __name__ == "__main__":
    main()
