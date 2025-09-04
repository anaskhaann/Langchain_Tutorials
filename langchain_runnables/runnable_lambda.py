from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()


# Custom word count logic for calculating the word count
def word_counter(text):
    return len(text.split())


# generate joke
joke_gen_chain = RunnableSequence(prompt, llm, parser)

# Generate joke as it is and its count of words
my_par_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        # One way
        # "count": RunnableLambda(lambda x: len(x.split())),
        # Second way
        "count": RunnableLambda(word_counter),
    }
)

# Connect joke and parallel chain
final_chain = RunnableSequence(joke_gen_chain, my_par_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)
print("=" * 60)
print(result["joke"])
print("=" * 60)
print(result["count"])
print("=" * 60)
print(f"Joke--> {result['joke']}, Word Count--> {result['count']}")


######################################

# def word_counter(text):
#     return len(text.split())

# runnable_counter = RunnableLambda(word_counter)
# runnable_counter.invoke('This will count the words based on space')
