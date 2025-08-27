from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = PromptTemplate(
    template="Give me 3 facts about {topic}.", input_variables=["topic"]
)

parser = StrOutputParser()

# Here we will create chain for our model and prompt

chain = template | model | parser

result = chain.invoke({"topic": "UFC"})

print(result)

print("===========================")
print("Visualize the chain")
chain.get_graph().print_ascii()
