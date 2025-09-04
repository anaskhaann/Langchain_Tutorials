from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the joke from {response}", input_variables=["response"]
)

parser = StrOutputParser()

# generate joke
joke_gen_chain = RunnableSequence(prompt1, llm, parser)

# Generate joke as it is and its explaination
my_par_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explaination": RunnableSequence(prompt2, llm, parser),
    }
)

# Connect joke and parallel chain
final_chain = RunnableSequence(joke_gen_chain, my_par_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)
print("=" * 80)
print(result["joke"])
print("=" * 80)
print(result["explaination"])
