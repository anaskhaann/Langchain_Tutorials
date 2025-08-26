from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# connect to api
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model = ChatHuggingFace(llm=llm)


# create a parser for json
parser = JsonOutputParser()


template = PromptTemplate(
    template="Give me 5 facts about {topic}. \n {format_instruction}",
    input_variables=["topic"],
    # This is used in json output format we need to pass a parser to get the json format
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

"""
Is we want output as 
fact1: ...
fact2: ...
fact3: ...
fact4: ...
fact5: ...
Then we cannot do so. because llm enforce its default schema
"""


# template --> model --> prompt --> format with json --> result --> parser --> final result

chain = template | model | parser

result_with_chain = chain.invoke({"topic": "black hole"})

print(result_with_chain)
