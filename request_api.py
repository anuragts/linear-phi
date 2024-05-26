from dotenv import load_dotenv
import aiohttp
import asyncio
import os

load_dotenv()

API_KEY = os.getenv("LINEAR_API_KEY")

async def get_linear_issues():
    url = "https://api.linear.app/graphql"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
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
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json={'query': query}) as response:
            print(await response.text())  # Print the text response asynchronously
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Query failed to run by returning code of {response.status}. {await response.text()}")

async def main():
    issues = await get_linear_issues()
    print(issues)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
