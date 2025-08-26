from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
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

# Create a parser
parser = StrOutputParser()


# Below flow in chain
"""
prompt1 = template1.invoke({"topic": "Black Hole"})
result1 = llm.invoke(prompt1)
prompt2 = template2.invoke({"text": result1.content})
result2 = llm.invoke(prompt2)
"""

# template1 --> llm then convert it to string with parser --> then that parsed output went to template2 --> llm --> result is parsed in string
chain = template1 | llm | parser | template2 | llm | parser

# invoke the chain with prompt

result = chain.invoke({"topic": "black hole"})
# this prompt will go to template1 and then chain starts

print(result)
