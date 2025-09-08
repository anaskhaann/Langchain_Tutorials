from langchain_community.tools import DuckDuckGoSearchRun

"""These tools are runnables"""

# create tool
search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("top new in India today")

print(result)
