import numpy as np
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()


embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# our predefined document
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",
]

query = "Tell me about Virat Kohli"

# first document embeddings

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)


# now check similarity between query and document embedding

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

# enumerate to attach a number with each output and then if we sort then positioning will still be available
# sorting based on score value not on index
print(sorted(list(enumerate(scores)), key=lambda x: x[1]))

# now extract the highest
index, high_score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]


# Now print the result
print(query)
print("------------------------------------")
print(documents[index])  # from document select the index which has highest score
print("------------------------------------")
print(f"Similarity score is:{round(high_score * 100, 2)}")
