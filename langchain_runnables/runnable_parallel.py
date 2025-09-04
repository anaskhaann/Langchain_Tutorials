from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

prompt = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt, llm, parser),
        "linkedin": RunnableSequence(prompt2, llm, parser),
    }
)

# print(parallel_chain.invoke({"topic": "Runnables in Langchain"}))
result = parallel_chain.invoke({"topic": "Runnables in Langchain"})

print(result)
print("=" * 50)
print(result["tweet"])
print("=" * 50)
print(result["linkedin"])
