# -*- coding: utf-8 -*-

import requests
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Just for testing

search_tool = DuckDuckGoSearchRun()

search_tool.invoke("Top news in India Today")

# create llm

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# test llm
llm.invoke("Who are you?")

# Create agent out of llm
from langchain import hub  # hub for predefined prompt
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)  # for creating agent and making it executable

"""
REACT Agent:
Reasoning and Action.
"""

# get the prompt design pattern for react from hub
# This is the predefined prompt for react agent
prompt = hub.pull("hwchase17/react")

"""
Create react agent by
1. Which llm used
2. which tools available
3. which prompt
"""

agent = create_react_agent(llm=llm, tools=[search_tool], prompt=prompt)

"""**Agent Thinks and Plan and Agent Executor Execute the works**

"""

"""Create executor of the Agent"""
"""
1. specify tools
2. specify agents
3. Verbose = True (This helps to show thinking of the Agent)
"""

agent_executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)

# Test by checking response
response = agent_executor.invoke(
    {"input": "What are the most efficient platforms to Learn Development in 2025"}
)

print(response)

print(response["output"])

# Test by checking response
response = agent_executor.invoke(
    {"input": "What is the population of capital on India"}
)

print(response["output"])

# Add another tool to get weather of the city
# using free Api for Us only


@tool
def get_temperature(city_name: str) -> float:
    """This function get the current weather data for a given city"""
    url = f"https://goweather.xyz/weather/{city_name}"

    response = requests.get(url)
    return response.json()


llm

agent = create_react_agent(llm=llm, tools=[search_tool, get_temperature], prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent, tools=[search_tool, get_temperature], verbose=True
)

result = agent_executor.invoke(
    {"input": "What is the capital of Germany. Also find its temperature"}
)

print(result)

result["output"]

"""This is not the capable way to Scale and create Solid Ai Agents.

For that we need to Study **Langraph**

"""
