from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        SystemMessage(content="You are a helpful {domain} expert"),
        HumanMessage(content="Explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

"""
The problem is we are getting place holder as it is.
It is not replacing dictionary values.
"""

print(prompt)
