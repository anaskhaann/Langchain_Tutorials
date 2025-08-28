## Chains in LangChain

In LangChain, you rarely make just a single call to an LLM. More complex applications require linking multiple components together. **Chains** are the fundamental concept for creating these multi-step, coherent workflows.

---

#### What Are Chains and Why Use Them?

A **chain** is a sequence of connected components, where the output of one component becomes the input for the next. Think of it like a factory assembly line: raw materials (your initial input) go in one end, and each station (a component like a prompt, model, or parser) performs an operation before passing it to the next, resulting in a finished product (the final output).

We use chains to build applications that are more powerful than a single LLM call, such as:

- Answering questions over specific documents.
- Interacting with APIs.
- Making decisions and taking actions.

At its core, chaining is powered by the **LangChain Expression Language (LCEL)**, which uses the pipe (`|`) symbol to link components together.

---

#### 1. Simple Chains

A simple chain is the most basic type: a linear sequence of components. The most common pattern is **Prompt + Model + Output Parser**.

- **When to Use:** This is the foundation for almost any LLM-powered task, like summarization, extraction, or answering a direct question.
- **How to Use:**

  1.  Define your `PromptTemplate`.
  2.  Instantiate your `ChatModel`.
  3.  Choose an `OutputParser`.
  4.  Pipe them all together using `LCEL (|)`.

  ```python
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_openai import ChatOpenAI
  from langchain_core.output_parsers import StrOutputParser

  # The chain is created by linking the components
  simple_chain = ChatPromptTemplate.from_template(...) | ChatOpenAI() | StrOutputParser()
  ```

---

#### 2. Sequential Chains

A sequential chain involves at least two distinct steps, where the output from the first step is used as the input for the second step.

- **When to Use:** When a task requires intermediate reasoning. For example, generating a company name (step 1) and then writing a slogan for that name (step 2).
- **How to Use:**

  1.  Create your first chain (`chain_one`).
  2.  Create your second chain (`chain_two`), ensuring its prompt can accept the output of the first.
  3.  Pipe the two chains together. LCEL automatically handles passing the output of the first as the entire input to the second.

  ```python
  # chain_one generates a company name from a product description
  # chain_two writes a slogan for a given company name
  sequential_chain = chain_one | chain_two
  ```

---

#### 3. Parallel Chains

Parallel chains allow you to execute multiple chains at the same time with the same input, and then merge their results into a single dictionary.

- **When to Use:** This is useful when you need to extract different kinds of information from the same input. For example, from a product review, you might want to generate a summary (chain A) and a sentiment score (chain B) simultaneously.
- **Runnable Overview:** This is achieved with `RunnableParallel` or, more commonly, by defining a dictionary where the keys are your desired output names and the values are the chains that will produce them.
- **How to Use:**

  1.  Define each of the chains you want to run in parallel (e.g., `summary_chain`, `sentiment_chain`).
  2.  Construct a dictionary that maps your desired output keys to these chains.

  ```python
  from langchain_core.runnables import RunnableParallel

  # Assume summary_chain and sentiment_chain are already defined
  parallel_chain = RunnableParallel(
      summary=summary_chain,
      sentiment=sentiment_chain,
  )
  ```

  When you invoke this, the input is passed to _both_ chains at once, and the final output will be a dictionary like `{'summary': '...', 'sentiment': 'Positive'}`.

---

#### 4. Conditional Chains (Branching)

Conditional chains allow you to introduce `if/else` logic into your workflow, routing the execution down different paths based on the input or the result of a previous step.

- **When to Use:** When your application needs to make decisions. For example, classifying an incoming query as either a "question" or a "statement" and then routing it to an "answer chain" or a "chat chain" accordingly.
- **Runnable Overview:** This is handled by `RunnableBranch`. It takes a series of `(condition, runnable)` pairs and a `default` runnable. It checks each condition in order and runs the runnable corresponding to the first condition that evaluates to `True`.
- **How to Use:**

  1.  Define the chains for each possible branch (e.g., `question_chain`, `chat_chain`).
  2.  Write a function that takes the input and returns `True` or `False` for a specific condition.
  3.  Construct the `RunnableBranch` with your conditions and chains.

  ```python
  from langchain_core.runnables import RunnableBranch

  # A function to check if the input contains a question mark
  def is_question(input_dict):
      return "?" in input_dict.get("query", "")

  # The branch defines the routing logic
  branch = RunnableBranch(
      (is_question, question_answer_chain), # If is_question is True, use this chain
      chat_chain # Default chain to use otherwise
  )
  ```

---

Made with ❤️ by Mohd Anas
