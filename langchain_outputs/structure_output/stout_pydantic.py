from typing import Literal, Optional

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

load_dotenv()

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
class Review(BaseModel):
    # set field for providing description
    key_theme: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list"
    )
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either negative, positive or neutral"
    )

    # the below are optional thus import optional
    pros: Optional[list[str]] = Field(
        default=None, description="Write all pros inside a list"
    )
    cons: Optional[list[str]] = Field(
        default=None, description="Write all cons inside a list"
    )
    name: Optional[str] = Field(
        default=None, description="Write the name of the reviewer"
    )


# tell the model to refer the above structure
structure_model = model.with_structured_output(Review)

# invoke structured model
response = structure_model.invoke(big_review)

print(response)

print("========================================================")
print(response.name)  # because it is from class

print("========================================================")
print(response.summary)

print("========================================================")
print(response.sentiment)
