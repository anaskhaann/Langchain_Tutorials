from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

"""we will need a infinite loop that will not exit the chat until user press the exit"""

while True:
    user_query = input("You: ")

    # if user type exit then break
    if user_query == "exit":
        break
    result = model.invoke(user_query)

    print(f"AI: {result.content}")
