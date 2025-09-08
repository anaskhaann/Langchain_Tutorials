from typing import Type

from langchain.tools import BaseTool
from pydantic import BaseModel, Field


# arg schema using pydantic
class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")


"""We need to create a class of our tool which will inherit from base tool"""


class MultiplyTool(BaseTool):
    # tool name
    name: str = "multiply"
    description: str = "Multiply two numbers"

    # schema of argument made through pydantic above
    args_schema: Type[BaseModel] = MultiplyInput

    # This is the name which should match it will run when the tool object is invoke
    def _run(self, a: int, b: int) -> int:
        return a * b


# Create a tool
multiply_tool = MultiplyTool()

# Run the tool

result = multiply_tool.invoke({"a": 4, "b": 7})

print(result)
