from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel, Field

load_dotenv()

# connect to api
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model = ChatHuggingFace(llm=llm)


# pydantic schema
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City of the person from where he belongs")


# parser
# we need to tell our pydantic object is of which class
parser = PydanticOutputParser(pydantic_object=Person)


# template
my_temp = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt = my_temp.invoke({"place": "Indian"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

print("=============== Same result with chain =============")

chain = my_temp | model | parser

chain_result = chain.invoke({"place": "chinese"})

print(chain_result)
