# all document loader are in langchain_community.document_loaders
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

# 1. We have to load the file using loader object
loader = TextLoader("./docs/cricket.txt", encoding="utf8")

# load the document
docs = loader.load()

print(docs)
print("=" * 50)
print(type(docs))
print("=" * 50)
print(len(docs))
print("=" * 50)
print(docs[0])
print("=" * 50)
print(type(docs[0]))
print("=" * 50)
print((docs[0].page_content))
print("=" * 50)
print((docs[0].metadata))

# now we can do chaining with this text with llms
llm = ChatGroq(model="gemma2-9b-it")

# output parser
parser = StrOutputParser()

# prompt
prompt = PromptTemplate(
    template="Write a summary of the {poem}", input_variables=["poem"]
)

chain = prompt | llm | parser

response = chain.invoke({"poem": docs[0].page_content})

print("=" * 50)
print(response)
