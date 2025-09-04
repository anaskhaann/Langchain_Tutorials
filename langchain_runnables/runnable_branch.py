from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableBranch,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

prompt1 = PromptTemplate(
    template="Write a short report about {topic}", input_variables=["topic"]
)

# prompt when number of words > 500
prompt2 = PromptTemplate(
    template="Summarize the following {text}", input_variables=["text"]
)

parser = StrOutputParser()

# Sequencial chain for generating report
report_gen_chain = RunnableSequence(prompt1, llm, parser)

"""Since we are going to get the output of report chain from parser thus we need to check the condition of that"""
branch_chain = RunnableBranch(
    # if length of report is 500 then summarize
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, llm, parser)),
    # if length is < 500 then print as it is
    # this can be our default chain also
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)


result = final_chain.invoke({"topic": "Runnable Branch"})

print(result)
