## **Retrievers in LangChain**

After setting up a vector store, you need a way to fetch information from it. In LangChain, this is handled by a **Retriever**. Retrievers are a core component that makes Retrieval-Augmented Generation (RAG) powerful and flexible, going far beyond simple database lookups.

---

## What are Retrievers?

A **Retriever** is a standard LangChain interface that takes a string query as input and returns a list of relevant `Document` objects as output. Its sole purpose is to fetch the most appropriate data for a given question.

While they are most commonly used to retrieve from a vector store, they can be configured to fetch documents from any source, including APIs, databases, or other specialized tools.

---

## Retriever vs. Vector Store Similarity Search

This is a crucial distinction.

- A **Vector Store's `.similarity_search()`** is a specific method on a vector store object. It's a direct, concrete function that finds documents based on vector closeness.
- A **Retriever** is a more **general abstraction**. The standard `VectorStoreRetriever` _uses_ the `.similarity_search()` method under the hood, but the retriever interface is much more powerful. It standardizes the act of "fetching," allowing you to swap out simple retrievers for more advanced ones without changing the rest of your chain.

**Analogy**: A vector store is like a car's engine—powerful and essential. A retriever is like the whole car—it uses the engine but adds a steering wheel, brakes, and navigation (i.e., more advanced logic) to control how the fetching is done.

---

## Types of Retrievers

Retrievers can be categorized in several ways, but a helpful approach is to think of them in two groups:

**Data Source Based Retrievers**

These are defined by _where_ they get the documents from. They are direct connections to a knowledge source.

These focus on specific data origins, pulling from external or structured sources: -

- **Examples**: WikipediaRetriever (from Wikipedia), WebBaseLoader as retriever (from web pages), Amazon Kendra Retriever (enterprise search), ElasticSearch Retriever (from ES indices). -

- **How They Work**: They connect to the source API/index, execute queries, and return docs. Often combined with loaders for ingestion.

**Searching Mechanism Based Retrievers**

These are defined by _how_ they search for or process documents. They often wrap another retriever (like a vector store retriever) and add more sophisticated logic on top.

These emphasize algorithms for querying and ranking:

- **Examples**: VectorStoreRetriever (similarity), MMR Retriever (diversity), MultiQueryRetriever (query expansion), ContextualCompressionRetriever (post-filtering), EnsembleRetriever (combining multiple).
- **How They Work**: They apply techniques like embedding similarity, reranking, or LLM augmentation to improve relevance beyond basic search.

---

## 1. Wikipedia Retriever

**What It Is**: A retriever that queries Wikipedia for articles matching the query, returning summaries as documents.

**How It Works**: Uses the Wikipedia API to search for pages (via langchain_community.retrievers.WikipediaRetriever). Parameters include load_max_docs (default 1), lang (default English). It fetches page summaries and metadata (e.g., title, URL). Internally, it loads via WikipediaLoader and retrieves top-k matches.

Code:

```python
from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever(load_max_docs=2)
docs = retriever.get_relevant_documents("LangChain")
```

---

## 2. Vector Store Retriever

**What It Is**: A wrapper turning any VectorStore into a retriever for similarity-based document retrieval.

**How It Works**: Embeds the query, searches the vector store using metrics like cosine similarity, and returns top-k documents. Supports filters (e.g., metadata) and search types (similarity, mmr). Created via `vectorstore.as_retriever(search_kwargs={"k": 5})`.

Code example:

```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(["text1", "text2"], embeddings)
retriever = vectorstore.as_retriever()
docs = retriever.get_relevant_documents("query")
```

---

## 3. Maximum Marginal Relevance (MMR) Retriever

- **What it is**: A retriever designed to fetch documents that are both **relevant** to the query and **diverse** from each other, avoiding redundancy.
- **How it Works**:

  1.  It first fetches a larger set of documents (e.g., 20) using standard similarity search.
  2.  It then iteratively selects documents for the final result. At each step, it chooses the document that is most similar to the query but _least_ similar to the documents already selected.

  - **Result**: Instead of getting four document chunks that all repeat the same information, you get four chunks that are all relevant but cover different aspects of the topic.

Code example:

```python
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.5})
docs = retriever.get_relevant_documents("query")
```

---

## 4. `MultiQueryRetriever`

- **What it is**: A retriever that improves search results by rephrasing the user's query from multiple perspectives.
- **How it Works**:
  1.  It takes the user's original query (e.g., "What are the side effects of paracetamol?").
  2.  It uses an LLM to generate several different versions of that query (e.g., "paracetamol adverse effects," "dangers of taking paracetamol").
  3.  It performs a separate vector search for _each_ of the generated queries.
  4.  It collects all the results and returns the unique set of documents. This helps find relevant documents that might have been missed by the original phrasing.

Code example:

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
retriever = MultiQueryRetriever.from_llm(retriever=vectorstore.as_retriever(), llm=llm)
docs = retriever.get_relevant_documents("query")
```

---

## 5. `ContextualCompressionRetriever`

- **What it is**: A powerful retriever that fetches documents and then filters or compresses their content _after_ retrieval to keep only the most relevant information.
- **How it Works**:
  1.  It wraps a **base retriever** (like a standard `VectorStoreRetriever`).
  2.  It first fetches a set of documents using the base retriever.
  3.  It then passes each fetched document and the original query to a **Document Compressor**.
  4.  The compressor reads the document and extracts _only the sentences or phrases_ that are directly relevant to the query, throwing away the rest.
  - **Result**: The context sent to the final LLM is much cleaner, more concise, and less noisy, which often leads to better and more accurate answers.

Code example:

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAI
llm = OpenAI()
compressor = LLMChainExtractor.from_llm(llm)
retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=vectorstore.as_retriever())
docs = retriever.get_relevant_documents("query")
```

---

## 6. Other Types of Retrievers

- VectorStoreRetriever
- SelfQueryRetriever
- EnsembleRetriever
- ContextualCompressionRetriever
- TimeWeightedRetriever
  Etc....

---

Made with ❤️ by Mohd Anas
