from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# to store the context
chat_history = []

"""we will need a infinite loop that will not exit the chat until user press the exit"""

while True:
    user_query = input("You: ")
    chat_history.append(user_query)

    if user_query == "exit":
        break
    result = model.invoke(chat_history)

    # append the result to the chat_history also
    chat_history.append(result.content)

    print(f"AI: {result.content}")


print(chat_history)