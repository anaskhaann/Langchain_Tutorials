# Tools in LangChain

While Large Language Models (LLMs) are masters of text and reasoning, their knowledge is static and they cannot interact with the outside world. **Tools** are the fundamental components in LangChain that solve this problem, giving LLMs new and powerful capabilities.

---

## What are Tools and How are They Helpful?

A **Tool** is an interface that an LLM can use to interact with external systems. Think of it as giving a brain access to arms, legs, and senses. By themselves, LLMs can only process and generate text. With tools, they can:

- **Access Live Information**: Look up current events on Google, search for scientific papers on ArXiv, or query Wikipedia.
- **Perform Calculations**: Use a calculator or a Python REPL for precise mathematical tasks.
- **Interact with APIs**: Query a database, book a flight, or check the weather.
- **Take Real-World Actions**: Send emails, post to social media, or control other software.

Tools are the bridge between the LLM's reasoning engine and the world's data and APIs.

---

## Tools and Agents: A Symbiotic Relationship

Tools are most powerful when used by an **Agent**.

- An **Agent** is the reasoning engine, powered by an LLM, that acts as a smart decision-maker.
- **Tools** are the set of actions the agent can choose from.

The agent examines a user's request, looks at the descriptions of the available tools, and decides _which_ tool to use (and with what inputs) to best answer the request. The agent is the "worker," and the tools are its "toolbox."

---

## **Types of Tools**

## 1. Built-in Tools

LangChain provides a wide array of pre-made tools for common tasks. These are ready to be used out-of-the-box. Examples include:

- `DuckDuckGoSearchRun`: For searching the web.
- `WikipediaQueryRun`: For querying Wikipedia.
- `SQLDatabaseToolkit`: A set of tools for interacting with SQL databases.

## 2. Custom Tools

These are tools you create yourself to perform specific tasks, such as:

- Querying your company's internal product database.
- Interacting with a proprietary API.
- Accessing a specific set of files on your local machine.

---

## How to Create Custom Tools

Creating your own tools is easy and can be done in several ways, from simple to advanced.

### 1. The `@tool` Decorator (Easiest)

This is the simplest way to turn any Python function into a LangChain tool.

- **How it Works**: Simply write a standard Python function with type hints and a clear docstring. Applying the `@tool` decorator automatically converts it into a `Tool` object. The **docstring is crucial**, as it becomes the description the agent uses to decide when to use the tool.
- **Example**:

  ```python
  from langchain.tools import tool

  @tool
  def multiply(a: int, b: int) -> int:
      """Multiplies two integers together. Use this for math questions."""
      return a * b
  ```

### 2. Using `StructuredTool` (More Control)

This method is useful when your tool requires multiple, complex arguments that can be best defined with a Pydantic model.

- **How it Works**: You define a function and then wrap it with `StructuredTool.from_function()`. This gives you more explicit control over the tool's input schema, which helps the agent provide the correct arguments.

### 3. Inheriting from `BaseTool` (Most Powerful)

This is the most advanced method, giving you complete control over every aspect of the tool.

- **How it Works**: You create a class that inherits from `BaseTool` and implement the `_run` method for synchronous execution and optionally the `_arun` method for asynchronous execution. This method is best when your tool needs to manage internal state or has complex logic that doesn't fit into a simple function.

---

## Toolkits

A **Toolkit** is a pre-packaged collection of related tools designed to give an agent a specific, broad capability.

- **What it is**: Instead of you having to find and initialize multiple tools individually, a toolkit bundles them together. For example, the `SQLDatabaseToolkit` includes tools for listing tables, inspecting schemas, and executing queries.
- **Benefit**: Toolkits are a convenient way to quickly equip an agent with the necessary abilities to interact with a complex system like a database or a specific API.

---

Made with ❤️ by **Mohd Anas**
