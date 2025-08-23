"""
Example for converting multiple string to embedding
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]

# use embed_documents instead of query
result = embedding.embed_documents(documents)

print(str(result))
