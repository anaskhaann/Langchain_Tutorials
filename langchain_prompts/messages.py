from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [
    SystemMessage(content="You are a helpfull assistent"),
    HumanMessage(content="Tell me about Langchain"),
]

result = model.invoke(messages)

# convert the response to AI message and store to messages
messages.append(AIMessage(result.content))

print(messages)
