import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  # for prompt template
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

"""Create a prompt template(dynamic) and take input
This shows how your prompt is going to look like
"""

my_template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}  
    Explanation Length: {length_input}  
    1. Mathematical Details:  
        - Include relevant mathematical equations if present in the paper.  
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
    2. Analogies:  
        - Use relatable analogies to simplify complex ideas.  
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,  # just to check if template is in f string or not
)

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
