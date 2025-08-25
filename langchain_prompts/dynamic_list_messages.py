from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# create chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent"),
        # now this query will not be understood by our customer support because it has some history related to current query so insert a message place holder
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ],
)

chat_history = []

# load history
with open("message_placeholder_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# prompt from template: this will replace variables to values
prompt = chat_template.invoke(
    {"chat_history": chat_history, "query": "Where is my refund?"}
)

print(prompt)
