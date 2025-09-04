from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

loader = PyPDFLoader("./docs/sample.pdf")

docs = loader.load()

# print(docs)
print("=" * 60)
print(len(docs))
print("=" * 60)
# content of 1st page
# print(docs[0].page_content)
# print("=" * 60)
# print(docs[1].page_content)
# print("=" * 60)
# print(docs[0].metadata)
# print("=" * 60)
# print(docs[1].metadata)

llm = ChatGroq(model="gemma2-9b-it")

# output parser
parser = StrOutputParser()

# prompt
prompt = PromptTemplate(
    template="Tell me about skills of a person from {resume}",
    input_variables=["resume"],
)

chain = prompt | llm | parser

result = chain.invoke({"resume": docs[0].page_content})

print("========= Result =========")
print(result)
