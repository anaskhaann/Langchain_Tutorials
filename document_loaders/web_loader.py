from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

url = "https://anaskhaann.vercel.app/"


loader = WebBaseLoader(url)

docs = loader.load()

print(docs)
print("=" * 60)
print(len(docs))
print("=" * 60)
print(docs[0])
print("=" * 60)
print(docs[0].page_content)


llm = ChatGroq(model="gemma2-9b-it")

# output parser
parser = StrOutputParser()

# prompt
prompt = PromptTemplate(
    template="Explain what is the {url} about",
    input_variables=["url"],
)

chain = prompt | llm | parser

result = chain.invoke({"url": docs[0].page_content})

print("========= Result =========")
print(result)

# prompt = PromptTemplate(
#     template='Answer the following question \n {question} from the following text - \n {text}',
#     input_variables=['question','text']
# )

# parser = StrOutputParser()

# url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
# loader = WebBaseLoader(url)

# docs = loader.load()


# chain = prompt | llm | parser

# print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))
