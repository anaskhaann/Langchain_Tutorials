from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# to store the context
chat_history = [SystemMessage(content="You are a helpfull assistent.")]

while True:
    user_query = input("You: ")
    # append as Human message
    chat_history.append(HumanMessage(content=user_query))

    if user_query == "exit":
        break
    result = model.invoke(chat_history)

    # append the result to the chat_history also
    chat_history.append(AIMessage(content=result.content))

    print(f"AI: {result.content}")


print(chat_history)
