import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

from dotenv import load_dotenv
load_dotenv()

browser = Browser(
	config=BrowserConfig(
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
        # windows: C:\Program Files\Google\Chrome\Application\chrome.exe
        # mac: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
		chrome_instance_path='C:\Program Files\Google\Chrome\Application\chrome.exe',
	)
)

async def main():
    agent = Agent(
        task="Go to https://github.com/zimo27/BrowserUse/issues/5, checkout the instructions and checkout the links specified in the issue",
        llm=ChatOpenAI(model="gpt-4o"),
        browser=browser,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())