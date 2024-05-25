import json

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat


MAX_TOKENS = 1500
AI_MODEL = "gpt-4o"

def useLinearAPI():
    return




assistant = Assistant(
    name="leapflow_linear",
    llm=OpenAIChat(
        model=AI_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=1,
    ),
    tools=[useLinearAPI],
    show_tool_calls=True,
    debug_mode=True,
)

assistant.print_response("Summarize the top stories on hackernews?")

