from langchain.tools import tool

"""
1. Create functions to make them tool.
2. Create a class of Toolkit, name of the class will be name of tool kit
3. Define a method inside to get list of all tools and return the tools which it will use
4. Create object of toolkit
5. get_tools from toolkits
6. Access tools either by loop or using OOPs concept
"""


@tool
def multiply_num(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


@tool
def square_num(a: float) -> float:
    """Give square of a number"""
    return a**2


@tool
def divide_num(a: float, b: float) -> float:
    """Divide two numbers"""
    if (a == 0) or (b == 0):
        return "Cannot Divide By Zero"

    return round((a / b), 2)


# Create a class of Toolkit
class MathToolKit:
    def get_tools(self):
        return [multiply_num, square_num, divide_num]


# object of toolkit
My_toolkit = MathToolKit()

# list of all tools
my_tools = My_toolkit.get_tools()

print(my_tools)

for i in my_tools:
    print(i.name)
    print("=" * 50)
    print(i.description)
