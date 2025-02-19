from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="My github username is qqq89898, my password is qqq_password_2789898, Go to https://github.com/zimo27/BrowserUse/issues/3, checkout the instructions and go to all the links specified in the issue, then login to github",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
