from google.adk.agents import Agent

from adk_agent.prompt import ROOT_AGENT_INSTRUCTION
from adk_agent.tools import count_characters

root_agent = Agent(
    name="adk_agent",
    model="gemini-2.0-flash",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)