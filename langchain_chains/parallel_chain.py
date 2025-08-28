from dotenv import load_dotenv

# for parallel chain import RunnableParallel
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Generate a short notes for the following {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate a 5 questions for the following {topic}",
    input_variables=["topic"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and question into a single document. \n notes -> {notes} question -> {ques}",
    input_variables=["notes", "ques"],
)

parser = StrOutputParser()

# TO run parallel chain we need to import RunnableParallel

# parallel chain will be made using RunnableParallel
parallel_chain = RunnableParallel(
    {
        # chain1
        "notes": prompt1 | model1 | parser,
        # chain2
        "ques": prompt2 | model2 | parser,
    }
)

# Merge chain is sequential chain
merge_chain = prompt3 | model2 | parser

# final chain is also sequential
final_chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = final_chain.invoke({"topic": text})

print(result)
print("=====================================")
print("Chain Visualization")
print("=====================================")

final_chain.get_graph().print_ascii()
