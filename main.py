import json
import os
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from dotenv import load_dotenv
import requests

load_dotenv()


API_KEY = os.getenv("LINEAR_API_KEY")

MAX_TOKENS = 1500
AI_MODEL = "gpt-4o"

def useLinearAPI():
    return


def get_linear_issues():
    url = "https://api.linear.app/graphql"
    headers = {
        "Authorization": f"{API_KEY}",
        "Content-Type": "application/json"
    }
    query = """
    {
      issues {
        nodes {
          id
          title
          description
        }
      }
    }
    """
    response = requests.post(url, headers=headers, json={'query': query})
    print(response.text)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")





assistant = Assistant(
    name="leapflow_linear",
    llm=OpenAIChat(
        model=AI_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=1,
    ),
    tools=[get_linear_issues],
    show_tool_calls=True,
    debug_mode=True,
)

assistant.print_response("What are the top 5 issues in linear?")

