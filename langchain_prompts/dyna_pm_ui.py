import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header("Testing for Dynamic Prompt: Research Tool")

"""This is the example of dynamic prompt"""

# multiple input dropdown for selecting paper
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

# multiple input dropdown for selecting style
style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

# multiple input dropdown for selecting length
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# load template from json
my_template = load_prompt("template.json")


# create a prompt with our template by taking the user given inputs
prompt = my_template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    }
)

# if button is pressed
if st.button("Tap to Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
