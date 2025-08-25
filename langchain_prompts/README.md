#### Prompts

It is nothing but a input given to our llm.
It is most important part because the output of the llm is heavily depend on the prompt given to it.

- For any LLM there are 2 kinds of prompt:
  Text Based
  Text + external source such as images etc(multimodel llms)

---

#### Single Prompts

These are a prompts where each time there is only one input string and output string.
The user can provide two types of prompts in this

1. Static Prompt
2. Dynamic Prompt

**Static Prompt:**

> These are the prompt where user give the entire prompt and have full control on the prompt. Each time user need to change the entire prompt if he needs a new response.

**Dynamic Prompt:**

> These are the prompt where user give the important parameters of the prompts and we have the control over the prompt. Example our Research Paper one.

For Dynamic Prompt these are the steps that needs to be done.

- `Prompt Template` is used.
- Create a template for how your prompt should look like and place the variables which user is going to fill.
- Then pass this template to the prompt along with the variables taken from user input.
- then pass the prompt to model.

---

#### Messages

For a Chat like conversation where we have a list of messages there are 3 categories in it.
These categories are used to store message history along with the label to it to identify the type of response.

1. `System Message:` These are the top level prompts which we define at the system level. for example: You are a helpfull assistant, you are expert doctor etc...

2. `Human Message:` This is nothing but the input prompt which user gives to the model

3. `AI Message:` This is the response generated from llm.

---

**Dynamic List of Message**

`ChatPromptTemplate` is used for this purpose.

It is similar to prompt template but in this we can make the systemMessage, Human Message dyanmic.

- This uses tuple rather than the previous behaviour of Prompt Template which uses `SystemMessage` methods.
- we simply pass the tuple of (role, prompt) in template
  ```py
  ("system", "You are a helpful {domain} expert"),
  ("human", "Explain in simple terms, what is {topic}")
  ```

`MessagePlaceHolder` in Langchain is a special placeholder used inside `ChatPromptTemplate` to dynamically insert the list of messages at run time

> Suppose we have a Customer assistant bot.
> His history is stored somewhere related to the refund/ transaction.
> He then make a new chat and new query regarding his refund.
> So we can use messageplace holders to load the history before this query.

---

Made with ❤️ by Mohd Anas Khan
