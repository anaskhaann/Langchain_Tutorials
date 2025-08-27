from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

# import structure outpar
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# connect to api

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model = ChatHuggingFace(llm=llm)

# Schema to guide llm

schema = [
    # send list of schema object
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic"),
]

# create parser based on the response schema
parser = StructuredOutputParser.from_response_schemas(schema)

template_prompt = PromptTemplate(
    template="Give me 3 facts about the {topic} \n {format_instructions}",
    input_variables=["topic"],
    # parse the output into the format which we will get from format instruction
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt = template_prompt.invoke({"topic": "milky way"})

print("===============Prompt Behind the Seen============")
print(prompt)
print("=================================================")

result = model.invoke(prompt)

print(result)
print("=================================================")
print(result.content)
print("=================================================")

final_result = parser.parse(result.content)

print("===================Final Result===================")
print(final_result)


############################## With Chains ############################

print("===================Final Result with Chain===================")
chain = template_prompt | model | parser

answer = chain.invoke({"topic": "milky way"})

print(answer)
