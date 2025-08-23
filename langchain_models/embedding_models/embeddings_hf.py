"""
Example for using open source
"""

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

document = ["This is the testing list", "I am Batman", "He is spiderMan"]

# vector = embedding.embed_query(text)
vector2 = embedding.embed_documents(document)

print(str(vector2))
