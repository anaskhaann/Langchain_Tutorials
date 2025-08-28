from typing import Literal

from dotenv import load_dotenv

# for conditional chain import RunnableBranch
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# parser for result
parser = StrOutputParser()


# feedback class for getting fixed output for sentiment
class feedback(BaseModel):
    sentiment: Literal["postive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


# parser for sentiment structure output
parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="classify the sentiments of the following text as postive or negative \n {text} \n {format_instructions}",
    input_variables=["text"],
    partial_variables={
        "format_instructions": parser2.get_format_instructions()
    },  # get format instruction from pydantic parser
)

prompt2 = PromptTemplate(
    template="Reply in one line to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Reply in one line to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)


postive_feedback = "The is the superb smartphone with excellent battery life"

negative_feedback = "worst smartphone, i am very disappointed"

# chain to classsify sentiment
classifier_chain = prompt1 | model | parser2

"""
Now which chain will activate next is depend on the output of classifier_chain. So we will need to make sure that the output of this chain always remain consistent. Either positive or negative. 
Because llm may give a negative or positive text, thus we will need to make sure that the output is always either "positive" or "negative" 
"""

# result will always be either positive or negative
# print(classifier_chain.invoke({"text": postive_feedback}))


# Now need to create branches for conditional chain

branch_chain = RunnableBranch(
    # """pass a tuplse of (condition, chain to run)
    # If no condition is met then default chain will run,Since we do not have any default chain we can pass lambda that returns something.
    # And for this lambda we will need to make it runnable using RunnableLambda"""
    #    (condition, chain)
    (lambda x: x.sentiment == "postive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    # Make default chain lambda into runnable chain
    RunnableLambda(lambda x: "no sentiment found"),
)

final_chain = classifier_chain | branch_chain

result = final_chain.invoke({"text": negative_feedback})

print(result)

print("=====================================")
print("Chain Visualization")
print("=====================================")

final_chain.get_graph().print_ascii()
