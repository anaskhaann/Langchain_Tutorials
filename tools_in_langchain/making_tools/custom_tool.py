from langchain_core.tools import tool

"""
Step 1.Create a normal function

Step 2. Add typhint to functions so that our llms can know what this functions returns and with doc strings llm will understand what it does

Step 3. Add a tool function decorator 
"""


@tool
def multiple(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


@tool
def square_num(a: float) -> float:
    """Give square of a number"""
    return a**2


num_multiply = multiple.invoke({"a": 4, "b": 7})
num_square = square_num.invoke({"a": 7})

print(num_multiply)
print("=" * 60)
print(num_square)

"""Some attributes which are there in tools"""

print(multiple.name)
print(multiple.description)
print(multiple.args)
print("=" * 80)
print(square_num.name)
print(square_num.description)
print(square_num.args)


"""The below is the thing which our llm get.
LLM does not get the tool it gets the schema"""

print(multiple.args_schema.model_json_schema())
print("=" * 70)
print(square_num.args_schema.model_json_schema())
