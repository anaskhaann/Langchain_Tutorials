## Document Loader

Large Language Models (LLMs) have a vast general knowledge, but they don't know about your specific, private data. To build powerful applications like a chatbot for your company's PDFs, you first need to load that data. **Document Loaders** are the tools that handle this crucial first step.

all document loaders are in `langchain_community.document_loader`

---

## Why We Need Document Loaders

We need Document Loaders to bridge the gap between our external data sources (like files on a computer) and the LangChain ecosystem. Their primary job is to fetch data from a source and convert it into a standardized format that LangChain can understand and work with.

This standardized format is the `Document` object, which contains two main parts:

1.  **`page_content`**: A string holding the actual text content from the source.
2.  **`metadata`**: A dictionary containing information about the source (e.g., file path, page number, URL).

By converting everything into this common structure, the rest of the process, like text splitting and embedding, becomes much simpler.

---

## Common Document Loaders

LangChain supports over 150 different loaders. Here are some of the most essential ones.

1. Text Loader (`TextLoader`)

This is the simplest loader, designed for plain `.txt` files.

- **How it Works:** It reads the entire content of a text file and stores it in the `page_content` of a single `Document`.
- **How to Use:**

  ```python
  from langchain_community.document_loaders import TextLoader

  loader = TextLoader("path/to/your/file.txt")
  ```

2. CSV Loader (`CSVLoader`)

Used for loading data from Comma-Separated Values (`.csv`) files.

- **How it Works:** It treats each **row** in the CSV file as a separate `Document`. The `page_content` for each document is a string automatically formatted from that row's values.
- **How to Use:**

  ```python
  from langchain_community.document_loaders.csv_loader import CSVLoader

  loader = CSVLoader(file_path="path/to/your/data.csv")
  ```

3. PDF Loader (`PyPDFLoader`)

PDFs are one of the most common document types, but they are notoriously difficult to parse.

- **Behind the Scenes:** A PDF loader doesn't just "read" the text. It uses an underlying library (like `pypdf`) to programmatically open the PDF file, go through it page by page, and extract the text content from each one.
- **How it Works:** It creates a separate `Document` for **each page** of the PDF. The page number is automatically stored in the `metadata`.
- **Most Used Types:**
  - **`PyPDFLoader`**: The most common choice. It's pure Python and easy to install.
  - **`PyMuPDFLoader`**: Generally faster and can be more accurate, especially with complex layouts.
  - **`UnstructuredPDFLoader`**: Can handle complex PDFs with tables and images.
- **How to Use:**

  ```python
  from langchain_community.document_loaders import PyPDFLoader

  loader = PyPDFLoader("path/to/your/report.pdf")
  ```

4. Web Based Loader (`WebBaseLoader`)

This loader fetches content directly from a URL.

- **How it Works:** It sends a request to the given URL, downloads the HTML content, and then uses a parsing library (like BeautifulSoup) to extract the main text, stripping away all the HTML tags and boilerplate.
- **How to Use:**

  ```python
  from langchain_community.document_loaders import WebBaseLoader

  loader = WebBaseLoader("[Relevant Docs for pdf](https://python.langchain.com/docs/concepts/document_loaders/)")
  ```

5. Directory Loader (`DirectoryLoader`)

This is a powerful utility loader that can load all files from a folder at once.

- **How it Works:** You provide a path to a directory and specify which loader class to use (e.g., `PyPDFLoader`). It then finds all matching files in the directory and uses the specified loader to load them.
- **Glob Patterns:** You can control which files are loaded using `glob` patterns.
  - `"*.pdf"`: Load all files ending with `.pdf` in the main directory.
  - `"**/*.pdf"`: Recursively load all `.pdf` files from the directory and any subdirectories.
  - `"**/[!.]*"`: Load all files in all directories, ignoring hidden files.
- **How to Use:**

  ```python
  from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

  loader = DirectoryLoader(
      'path/to/your/pdfs/',
      glob="**/*.pdf",         # Load all PDFs recursively
      loader_cls=PyPDFLoader   # Use the PDF loader for each file
  )
  ```

---

## `load()` vs. `lazy_load()`

When you call a loader, you have two options for how the documents are loaded into memory.

- **`load()`**: This is the standard method. It loads **all** documents from the source into your computer's RAM at once and returns a complete list.

  - ✅ **Pros:** Simple to work with.
  - ❌ **Cons:** Can cause your program to crash if you're loading thousands of large files, as you might run out of memory.

- **`lazy_load()`**: This method is much more memory-efficient. It returns an **generator(iterator)**. A document is only loaded into RAM when you ask for it in a loop.
  - ✅ **Pros:** Uses very little memory, making it ideal for processing huge datasets.
  - ❌ **Cons:** The iterator can only be used once.

**Analogy:** `load()` is like downloading an entire movie before you can watch it. `lazy_load()` is like streaming the movie—you only download the small part you're watching right now.

```python
# This could use a lot of RAM
all_documents = loader.load()

# This is very memory-efficient
for document in loader.lazy_load():
    # Process each document one at a time
    print(document.metadata)
```

---

Made with ❤️ by **Mohd Anas**
