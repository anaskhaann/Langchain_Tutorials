from typing import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

test_review = """The hardware is great but the software feels bloated. There are too many pre-installed apps that i can't remove. Also, the UI looks outdated compare to other brands. Hoping for a software update to fix this."""


# model create
model = ChatGroq(model="openai/gpt-oss-20b")


# schema: how to structure the output
class Review(TypedDict):
    summary: str
    sentiment: str


# mainstep: make model to use review class
"""When we call the below method, behind the seen there is a prompt which is generated that use to structure the output."""
structure_model = model.with_structured_output(Review)

# result
# response = model.invoke(test_review)

# rather than making the normal model, invoke the structure mode
response = structure_model.invoke(test_review)

# now we don't need to get the content
print(response)
print("=================================")
print(response["summary"])
print("=================================")
print(response["sentiment"])
