import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Header for webpage

st.header("Testing for Dynamic Prompt")

"""
This is the example of static prompt because everytime user is giving full complete prompt. Which is not recommended because output is heavily depends on The input of the prompt
"""

user_input = st.text_input("Enter your query..")

# if button is pressed
if st.button("Tap to Chat"):
    # we have to take the user query from input
    result = model.invoke(user_input)
    st.write(result.content)


