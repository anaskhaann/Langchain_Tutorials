# import huggingface end point because we are using api
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# create a object from hugging face and provide the parameters needed

# 1. Establish connection with model using end point and then create object of the model
my_llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # url of model from hugging face website
    task="text-generation",  # what task we need to perform on this model
)


model = ChatHuggingFace(llm=my_llm)

response = model.invoke("What is the capital of India?")


# print(response)
print(response.content)
