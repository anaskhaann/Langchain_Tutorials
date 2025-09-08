from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

"""
Step 1.Create a pydantic Class

Step 2. Create Function which will be used when the tool is called,(typehinting in this functional is optional since we are already validating through pydantic)

Step 3. Create a Structure tool and pass description, which function to use, schema which needs to check validation
"""


# pydantic model
class MultiplyIntput(BaseModel):
    # define types
    a: int = Field(required=True, description="First Number to Multiply")
    b: int = Field(required=True, description="First Number to Multiply")


# function
def multiply_num(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


"""Create StructureTool from function"""
multiply_tool = StructuredTool.from_function(
    func=multiply_num,
    args_schema=MultiplyIntput,
    description="Multiply two numbers",
    name="Multiply",
)

"""Same for Square Tool"""


class SquareIntput(BaseModel):
    a: int = Field(required=True, description=" Number to do Square")


def square_num(a: float) -> float:
    """Give square of a number"""
    return a**2


square_tool = StructuredTool.from_function(
    func=square_num,
    args_schema=SquareIntput,
    description="return square of a number",
    name="sqaure",
)


num_multiply = multiply_tool.invoke({"a": 4, "b": 7})
num_square = square_tool.invoke({"a": 7})

print(num_multiply)
print("=" * 60)
print(num_square)

"""Some attributes which are there in tools"""

print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
print("=" * 80)
print(square_tool.name)
print(square_tool.description)
print(square_tool.args)


"""The below is the thing which our llm get.
LLM does not get the tool it gets the schema"""

print(multiply_tool.args_schema.model_json_schema())
print("=" * 70)
print(square_tool.args_schema.model_json_schema())
