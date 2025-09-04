import time

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path="./docs/test_dir/",
    # glob = file patterns we need to extract
    glob="*.pdf",
    # class type of loader
    loader_cls=PyPDFLoader,
)

# Calculate Loader time
start = time.time()
docs = loader.load()
end = time.time()
print(f"Time take by Load: {end - start}")

for i in docs:
    i.metadata

# print(len(docs))
# print("=" * 60)
# print(docs[0].page_content)
# print("=" * 60)
# print(docs[0].metadata)
# print("=" * 60)
# print(docs[-1].page_content)
# print("=" * 60)
# print(docs[-1].metadata)

"""Lazy Loading for huge number of files"""
# Calculate Loader time
start2 = time.time()
docs2 = loader.lazy_load()
end2 = time.time()
print(f"Time take by Lazy Load: {end2 - start2}")

for i in docs2:
    i.metadata
