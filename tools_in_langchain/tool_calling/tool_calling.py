from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

"""Create a tool"""


@tool
def multiply(a: float, b: float) -> float:
    """Given 2 numbers this tool return their multiplication"""
    return round(a * b, 2)


# print(multiply.invoke({"a": 3, "b": 5}))
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

"""We have a method in llm to binds list of tools we can connect"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# bind the tools with llm
llm_with_tools = llm.bind_tools([multiply])
# print(llm_with_tools)

"""Now in future if the llm thinks that if it need to use the tool for multiply then it will use that tool.
Not all llms have the capability for tool calling
"""

# testing
# while True:
#     question = input("Enter Query or enter q to exit: ")

#     if question.lower() == "q":
#         break
#     print(llm_with_tools.invoke(question))

"""The below are the two result for normal query and query which needs to call tool"""

# Query without tool
"""
Enter Query or enter q to exit:Hello who are you

content='I am a large language model, trained by Google.' additional_kwargs={} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'safety_ratings': []} id='run--45f291a2-1548-4048-96ca-f7e759f9df55-0' usage_metadata={'input_tokens': 55, 'output_tokens': 11, 'total_tokens': 66, 'input_token_details': {'cache_read': 0}}
"""

# Query with tool
"""
Enter Query or enter q to exit:what is the multiplication of 3 * 39?

content='' additional_kwargs={'function_call': {'name': 'multiply', 'arguments': '{"a": 3.0, "b": 39.0}'}} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'safety_ratings': []} id='run--12fd9491-00b7-4650-9c40-5b1986b4b56b-0' tool_calls=[{'name': 'multiply', 'args': {'a': 3.0, 'b': 39.0}, 'id': '0664458e-e282-4f08-9636-7528431d9ddf', 'type': 'tool_call'}] usage_metadata={'input_tokens': 62, 'output_tokens': 19, 'total_tokens': 160, 'input_token_details': {'cache_read': 0}}
"""
# See the content part of the both responses

# list of tool
# llm_with_tools.invoke(question).tool_calls


"""Now we will see tool execution"""

test = llm_with_tools.invoke("what is the multiplication of 3 * 39?")

# get list of tools the result use
# print(result.tool_calls)

# Selecting first tool
# print(result.tool_calls[0])

# Selecting arguments from first tool to send as input for execution
# print(result.tool_calls[0]["args"])


# Now execute the function
# Send full Tool Call
print(
    "This is the Tool Message\nWe get this message when we execute a tool:\n",
    multiply.invoke(test.tool_calls[0]),
)


# Only send the arguments from tool call
print(
    "This is done by only passing arguments from Tool Call which will give the final result:\n",
    multiply.invoke(test.tool_calls[0]["args"]),
)


"""Now send the entire flow to LLM to give proper answer from LLM"""

# First we create a Human Message
query = HumanMessage("what is the multiplication of 3 * 39?")

# add query to messages history
messages = [query]

result = llm_with_tools.invoke(messages)

# add result --> Ai message to messages history
messages.append(result)

print("=" * 100)
print(messages)
print("=" * 100)

# tool message --> get input from arguments of the result
tool_result = multiply.invoke(result.tool_calls[0])

# Append the tool message also
messages.append(tool_result)

print("=" * 100)
print("Now our Messages will have a Human Message, AI Message and Tool Message")
print(messages)
print("=" * 100)

"""Now we can get the final result from llm"""

final_output = llm_with_tools.invoke(messages)
print(final_output)
print(final_output.content)
