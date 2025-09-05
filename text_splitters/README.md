## Text Splitting in LangChain

After loading your documents, the next crucial step in any RAG (Retrieval-Augmented Generation) pipeline is **Text Splitting**. This process is essential for preparing your data to be used effectively with Large Language Models (LLMs).

---

## Why We Need Text Splitting

The primary reason for splitting text is the **context window limit** of LLMs. An LLM can't process an entire 500-page book at once; it can only handle a few thousand words at a time. Text splitting breaks down large documents into smaller, manageable chunks that fit within this limit.

## Benefits of Text Splitting

- **Fits Context Windows**: Ensures the text sent to the LLM doesn't exceed its processing capacity.
- **Improves Retrieval Quality**: For RAG, it's better to retrieve small, highly relevant chunks of text rather than an entire long document. This provides the LLM with more focused and useful context.
- **Reduces Cost & Latency**: Sending smaller chunks of text to the LLM is faster and cheaper, as most API pricing is based on the amount of text processed.

---

## Different Text Splitters

Choosing the right text splitter is a balance between simplicity and semantic coherence. We can group them into four main categories.

1. Length-Based Splitting (`CharacterTextSplitter`)

This is the most straightforward approach to splitting.

- **Working Principle**: It splits text simply by counting characters. You define a `chunk_size` (e.g., 500 characters) and a `separator` (e.g., a newline character `\n`). It slides a window across the text, creating chunks of the specified size. A `chunk_overlap` can be set to maintain some context between chunks.
- **Advantages** ✅
  - **Simple & Fast**: Very easy to use and computationally cheap.
  - **Predictable**: You have direct control over the exact size of your chunks.
- **Disadvantages** ❌
  - **Context-Unaware**: It's a "dumb" method that can cut sentences or even words in half, potentially breaking the semantic meaning.

```python
from langchain.text_splitter import CharacterTextSplitter
# This splitter will try to split on newlines first, then by character count.
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator="\n")
```

---

2. Text Structure-Based Splitting (`RecursiveCharacterTextSplitter`)

This is the **most common and recommended** general-purpose splitter.

- **Working Principle**: It's a "smarter," hierarchical approach. It's given a list of separators and tries to split on them in order. By default, it tries to split on double newlines (`\n\n` for paragraphs), then single newlines (`\n` for lines), then spaces, and finally, by individual characters. It recursively applies this logic to create chunks that are as semantically whole as possible.
- **Advantages** ✅
  - **Preserves Context**: Does a much better job of keeping related text, like paragraphs and sentences, together.
  - **Robust Default**: It's a great starting point for almost any kind of text document.
- **Disadvantages** ❌
  - **Formatting Dependent**: Its effectiveness still depends on the text being reasonably well-formatted with standard separators.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
# This is the recommended default splitter.
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
```

---

3. Document Structure-Based Splitting (`RecursiveCharacterTextSplitter` + `Language`)

This is a specialized splitter that understands the syntax and structure of programming languages.

- **Working Principle**: You provide a specific `Language` (like Python or JavaScript) from LangChain's `Language` enum. The splitter then uses a list of separators that are syntactically relevant to that language. For Python, it will try to split on class definitions, then function definitions, and so on. This keeps logical blocks of code together.
- **Advantages** ✅
  - **High Coherence for Code**: Creates highly logical chunks by keeping entire functions or classes intact, which is essential for code analysis and generation tasks.
- **Disadvantages** ❌
  - **Not General-Purpose**: It is only effective for the specific programming languages it supports and should not be used for plain text.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
# Define the language to get syntax-aware separators.
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=20
)
```

---

4. Semantic Meaning-Based Splitting (`SemanticChunker`)
   This is the most advanced and context-aware method of splitting text.

- **Working Principle**: Instead of looking at characters or separators, this splitter uses an **embedding model** to understand the meaning of the text. It calculates the semantic similarity between adjacent sentences and creates a split wherever there is a significant shift in topic. This results in chunks that are exceptionally focused and semantically consistent.
- **Advantages** ✅
  - **Highest Quality Chunks**: Produces the most contextually coherent chunks, which is ideal for high-quality RAG.
  - **Independent of Formatting**: Works based on meaning, so it's not affected by messy formatting.
- **Disadvantages** ❌
  - **Computationally Expensive**: It's slower and more costly because it requires making calls to an embedding model during the splitting process.
  - **Variable Chunk Size**: The size of the resulting chunks is less predictable.

```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

# This splitter requires an embedding model to work.
splitter = SemanticChunker(OpenAIEmbeddings())
```

---

Made with ❤️ by Mohd Anas
