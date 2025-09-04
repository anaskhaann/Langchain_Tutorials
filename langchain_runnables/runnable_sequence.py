from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

# chain = RunnableSequence(prompt, llm, parser)

# print(chain.invoke({"topic": "AI"}))

# Take this further
prompt2 = PromptTemplate(
    template="Explain the joke from {response}", input_variables=["response"]
)

chain2 = RunnableSequence(prompt, llm, parser, prompt2, llm, parser)

print(chain2.invoke({"topic": "AI"}))
