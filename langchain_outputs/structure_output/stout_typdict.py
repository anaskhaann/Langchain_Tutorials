from typing import Annotated, Literal, Optional, TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

test_review = """The hardware is great but the software feels bloated. There are too many pre-installed apps that i can't remove. Also, the UI looks outdated compare to other brands. Hoping for a software update to fix this."""

big_review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Salmon Bhoi
"""

# model create
model = ChatGroq(model="openai/gpt-oss-20b")


# schema: how to structure the output
class Review(TypedDict):
    key_theme: Annotated[
        list[str], "Write down all the key themes discussed in the review in a list"
    ]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[
        Literal["pos", "neg"],
        "Return sentiment of the review either negative, positive or neutral",
    ]

    # the below are optional thus import optional
    pros: Annotated[Optional[list[str]], "Write all pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write all cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


# mainstep: make model to use review class
"""When we call the below method, behind the seen there is a prompt which is generated that use to structure the output."""
structure_model = model.with_structured_output(Review)

response = structure_model.invoke(big_review)

print(response)

print("========================================================")
print(response["name"])

print("========================================================")
print(response["summary"])

print("========================================================")
print(response["sentiment"])
