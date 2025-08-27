# Output Parsers in LangChain

When working with Large Language Models (LLMs), we get back a text string. While this is great for chatbots, real-world applications often need the data in a specific, structured format. **Output Parsers** are essential LangChain components that bridge this gap. They are mainly used for the LLMs that does not have the capability to structure there outputs

---

#### What Are Output Parsers and Why Do We Need Them?

An **Output Parser** is a class that helps structure the output of an LLM. It's responsible for two key tasks:

1.  **Provide Formatting Instructions:** It tells the LLM _how_ to format its response (e.g., "Respond with a JSON object.").
2.  **Parse the Output:** It takes the raw string from the LLM and transforms it into a useful data structure like a dictionary or a custom Python object.

We need them to make LLM outputs **reliable and programmatically accessible**, saving us from writing fragile manual parsing logic.

---

#### Types of Output Parsers

We'll focus on four fundamental types, from the simplest to the most powerful. But there are lot more than that

1. `StrOutputParser`

This is the most basic parser. It simply returns the LLM's output as a standard string.

- **When to Use:** Perfect for when you just need a text response, like in chatbots, summarization, or simple Q&A.
- **How to Use:**

  1.  Import `StrOutputParser`.
  2.  Add it as the final step in your chain.

  ```python
  from langchain_core.output_parsers import StrOutputParser

  chain = prompt | model | StrOutputParser()
  ```

- **Pros:** ✅ Simple and fast.
- **Cons:** ❌ Provides no structure.

---

2. `JsonOutputParser`

This parser helps you get a JSON object (which becomes a Python dictionary) from the LLM.

- **When to Use:** When you need a dictionary and are interacting with APIs or systems that use JSON.
- **How to Use:**

  1.  Import `JsonOutputParser`.
  2.  Instruct the model in your prompt to generate **only a JSON object**.
  3.  Add the parser to the end of your chain.

  ```python
  from langchain_core.output_parsers import JsonOutputParser

  template = PromptTemplate(
    template="Give me the name, age and city of fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()},
  )

    prompt = template.format()

  chain = prompt | model | JsonOutputParser()
  ```

- **Pros:** ✅ Outputs a universal, dictionary-like format.
- **Cons:** ❌ No validation. No Schema Enforcement.The chain will fail if the LLM returns a malformed JSON string. Cannot Get output in required Schema.

---

3. `StructuredOutputParser`

This is a more robust way to get a dictionary. You explicitly define the fields you want.

- **When to Use:** When you want a dictionary but need to give the LLM more explicit instructions about the required fields than with the basic `JsonOutputParser`.
- **How to Use:**

  1.  Define your desired fields using `ResponseSchema`.
  2.  Create the parser using `StructuredOutputParser.from_response_schemas(...)`.
  3.  Get the formatting instructions from the parser and include them in your prompt.
  4.  Add the parser to the end of your chain.

  ```python
  from langchain.output_parsers import ResponseSchema, StructuredOutputParser

  response_schemas = [
      ResponseSchema(name="name", description="The name of the user."),
      ResponseSchema(name="age", description="The age of the user.", type="int")
  ]
  parser = StructuredOutputParser.from_response_schemas(response_schemas)
  ```

- **Pros:** ✅ The descriptions guide the LLM to produce more accurate output.
- **Cons:** ❌ Still no runtime validation or type coercion.

---

4. `PydanticOutputParser`

This is the **most recommended and powerful** parser for structured data. It uses the Pydantic library to create typed data models.

- **When to Use:** This should be your default choice for any task requiring reliable, validated, and type-safe structured data in Python.
- **How to Use:**

  1.  Define your data structure by creating a class that inherits from Pydantic's `BaseModel`.
  2.  Create an instance of `PydanticOutputParser`, passing your custom class to it.
  3.  Get formatting instructions from the parser and add them to your prompt.
  4.  Pipe the chain's output to the parser.

  ```python
  from langchain_core.pydantic_v1 import BaseModel, Field

  class UserInfo(BaseModel):
      name: str = Field(description="The name of the user")
      age: int = Field(description="The age of the user")

  parser = PydanticOutputParser(pydantic_object=UserInfo)
  ```

- **Pros:** ✅ Provides robust _validation_ and _type coercion_ (e.g., turns `"25"` into `25`).
- **Cons:** ❌ Requires the `pydantic` library.

---

#### Summary Comparison

| Parser                       | Output Type          | Validation & Type Coercion? | Best For...                                                                        |
| :--------------------------- | :------------------- | :-------------------------- | :--------------------------------------------------------------------------------- |
| **`StrOutputParser`**        | `str`                | ❌ No                       | Simple text generation, summarization, or chatbots.                                |
| **`JsonOutputParser`**       | `dict`               | ❌ No                       | Quick-and-dirty JSON extraction for APIs or simple data passing.                   |
| **`StructuredOutputParser`** | `dict`               | ❌ No                       | Getting a dictionary with more reliable field names than `JsonOutputParser`.       |
| **`PydanticOutputParser`**   | Pydantic `BaseModel` | ✅ Yes                      | **Most applications.** Building reliable, type-safe, and validated data pipelines. |

**Note:** Newer LangChain versions often favor the `.with_structured_output()` method on the LLM object, which internally uses these parsing concepts. However, understanding the individual parsers is key to mastering LangChain's data handling capabilities.

---

Made with ❤️ by Mohd Anas
