"""
Example for converting single string to embedding
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large", dimensions=32
)  # dimension is the shape which we are expecting to be of our vector

result = embedding.embed_query("Delhi is the capital of India")


# Convert the embedding to str to see
print(str(result))
