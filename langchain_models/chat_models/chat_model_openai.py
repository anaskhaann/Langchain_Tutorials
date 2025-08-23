from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# we can pass multiple parameter
# temperature: randomness --> lower the more deterministric
# max_token : how much we need to restrict the lenght of the output as per tokens

model = ChatOpenAI(model="gpt-4", temperature=0.4, max_completion_tokens=100)


response = model.invoke("What is the capital of India?")
# Now this response is of chat model so it will retun a dictionary of multiple info in which our answer is in content

print(response.content)
