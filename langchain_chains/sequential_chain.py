from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# prompt1
prompt1 = PromptTemplate(
    template="What is an {profession} and what do they do?",
    input_variables=["profession"],
)

# prompt2
prompt2 = PromptTemplate(
    template="Summarize the {text} in 5 bullet points.",
    input_variables=["text"],
)

# parser
parser = StrOutputParser()

# chain
chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({"profession": "Ai engineer"})

print(response)

print("=====================================")
print("Chain Visualization")
print("=====================================")

chain.get_graph().print_ascii()
