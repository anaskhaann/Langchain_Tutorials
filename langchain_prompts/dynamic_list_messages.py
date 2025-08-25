from langchain_core.prompts import ChatPromptTemplate

"""
The problem was we were getting place holder as it is.
It is not replacing dictionary values.
--> TO fix this problem we will pass heirarchical structure in tuple rather than using system messages.
"""

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

print(prompt)
