import json
from typing import Annotated

import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import InjectedToolArg, tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


"""
Step 1

Create 2 tools 
1. Get currency convertor factor
2. Multiple the factor
"""


# first tool
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This will get the currency conversion factor for between base currency and target currency"""

    # "https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/{base_currency}/{target_currency}
    # our url for api

    url = f"https://v6.exchangerate-api.com/v6/b7866a00b8f612e26cfddb0d/pair/{base_currency}/{target_currency}"

    # send request to the url
    response = requests.get(url)

    return response.json()


# we can invoke the tool to test the response
# get_conversion_factor.invoke({"base_currency": "USD", "target_currency": "INR"})


# 2nd tool
@tool
def convertor(
    base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]
) -> float:
    """
    given a currency conversion rate this function calculates the target currency value from a given base currency value
    """

    return base_currency_value * conversion_rate


# Test the multiplication is working or not
# convertor.invoke({"base_currency_value": 12, "conversion_rate": 33.2})


"""
Step 2. Bind the Tools with LLM

"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

llm_with_tool = llm.bind_tools([get_conversion_factor, convertor])


"""
Step 3

Tool Calling
"""

# create human message
messages = [
    HumanMessage(
        "What is the conversion factor between USD and INR, and based on that convert 10 USD to INR"
    )
]

# this will give us ai message
ai_message = llm_with_tool.invoke(messages)
"""This will wont wait for our conversion rate the other tool will have the Old conversion rate from its data thus we need InjectedTool.
This means that injected tool argument will be set by developer not the llm"""

# also append the ai message to message list
messages.append(ai_message)

# print(ai_message)
# print(ai_message.tool_calls)
# This wont have conversion rate for 2nd tool because we ar going to pass it

for tool_call in ai_message.tool_calls:
    # execute the 1st tool and get the value of conversion rate
    if tool_call["name"] == "get_conversion_factor":
        tool_message1 = get_conversion_factor.invoke(tool_call)

        # fetch conversion rate from the tool message, and append the message to list

        # since this is the object we have to first fetch the content and then convert it to json and fetch the conversion rate
        conversion_rate = json.loads(tool_message1.content)["conversion_rate"]

        # append
        messages.append(tool_message1)

    if tool_call["name"] == "convertor":
        # before executing the convertor we have to add manually the conversion rate which was not present earlier because we have made it injected
        # Since it is a dictionary add one more key to args key
        tool_call[args]["conversion_rate":conversion_rate]
        # This args is not an error since we know it is present in the tool message dictionary
        tool_message2 = convertor.invoke(tool_call)

        # append again
        messages.append(tool_message2)


"""
Pass the entire context to llm
"""

print(llm_with_tool.invoke(messages))
print("***** Final Answer is *****")
print(llm_with_tool.invoke(messages).content)
