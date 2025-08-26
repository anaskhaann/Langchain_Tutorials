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
    template="Give me the name, age and city of fictional person \n {format_instruction}",
    input_variables=[],
    # This is used in json output format we need to pass a parser to get the json format
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# here we dont invoke the template because we dont have any input variables, we only need to format our response
prompt = template.format()
# Return a JSON object. THis is the prompt which is generating behind the seen

# print(prompt)

result = model.invoke(prompt)
# result will contain json
print("==============================")
print("Before Parse")
print(result)

# parse the response for json
final_result = parser.parse(result.content)
print("==============================")
print("After Parse")
print("==============================")
print(final_result)
# Now we can fetch name, age and city of the final result

#################### WITH CHAINS #########################

print("==============================")
print("Same with Chains")
print("==============================")

# template --> model --> prompt --> format with json --> result --> parser --> final result

chain = template | model | parser

# blank dictionary because we dont have any input variables
result_with_chain = chain.invoke({})

print(result_with_chain)
