# import the library

from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

# create the object with model which we need to use
# we are using gpt open source model
llm = OpenAI(model="gpt-3.5-turbo-instruct")


# Invoke method is used to ask questions/prompts

result = llm.invoke("What is the capital of India?")

print(result)
