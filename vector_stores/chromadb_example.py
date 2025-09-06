"""Run this notebook in jupter cell for better results"""

from dotenv import load_dotenv
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

load_dotenv()


# Create langchain documents for ipl players
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)


# create list of docs
docs = [doc1, doc2, doc3, doc4, doc5]


# create a vectore store
vector_store = Chroma(
    # how we are doing embeddings
    embedding_function=GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    ),
    # where to store the embeddings
    persist_directory="my_chroma_db",
    # table name i.e collections sample
    collection_name="sample",
)


# add documents
vector_store.add_documents(docs)
"""Each document will be assigned a unique id.
But we can also decide how to pass unique id"""

# view documents
vector_store.get(include=["embeddings", "documents", "metadata"])


# search documents(similarity search)
vector_store.similarity_search(
    query="Who among these are a bowler?",
    k=1,  # k stands for how many similar objects we need to show
)


# search documents (similarity with score-->distance)
vector_store.similarity_search_with_score(query="Who among these are a bowler?", k=1)


# filtering over meta data
vector_store.similarity_search(
    query="",
    # filter are used to pass meta data
    filter={"team": "Chennai Super Kings"},
)


"""update document"""

# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"},
)

# pass the document id which we get at the time of creating the vector store document
vector_store.update_document(
    document_id="09a39dc6-3ba6-4ea7-927e-fdda591da5e4", document=updated_doc1
)


"""delete the document
pass the id's which we need to delete
"""

# delete document
vector_store.delete(ids=["09a39dc6-3ba6-4ea7-927e-fdda591da5e4"])

# view documents
vector_store.get(include=["embeddings", "documents", "metadatas"])
