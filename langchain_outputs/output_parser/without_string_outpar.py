from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# 1st template
template1 = PromptTemplate(
    template="Write a detail report on {topic}", input_variables=["topic"]
)
# 2nd template
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text./n {text}",
    input_variables=["text"],
)

# prompt 1 and response
prompt1 = template1.invoke({"topic": "Black Hole"})
result1 = llm.invoke(prompt1)

# prompt 2 and response from result 1
prompt2 = template2.invoke({"text": result1.content})
result2 = llm.invoke(prompt2)

print(result2.content)
