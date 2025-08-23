# import huggingface pipeline because we are downloading model locally
import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()

# download model to D drive
os.environ["HF_HOME"] = "D:/huggingface_cache"

my_llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # model id is same as url
    task="text-generation",
    pipeline_kwargs={"temperature": 0.5, "max_new_tokens": 100},
)


model = ChatHuggingFace(llm=my_llm)

result = model.invoke("What is the capital of India?")


# print(result)
print(result.content)
