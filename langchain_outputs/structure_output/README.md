## Structuring LLM Outputs with `with_structured_output` in LangChain

Large Language Models (LLMs) are incredibly powerful, but their default output is often unstructured text. This can be difficult to work with programmatically. LangChain's `.with_structured_output()` method provides a robust and elegant solution to force LLMs to return information in a specific, predictable format like JSON.
This is only applicable to LLMs that have a capability to convert response to structure format.

---

#### Unstructured vs. Structured Response

First, let's understand the problem we're solving.

- **Unstructured Response:** This is the default behavior of an LLM. It's free-form text, similar to how a human would write or speak. While easy for humans to read, it's difficult for a program to parse reliably.

  - _Example:_ Sure, the user's name is Anas, they are 22 years old, and their email is anas@email.com.

- **Structured Response:** This is a response formatted according to a predefined schema (like a Python class or a JSON object). It's predictable, easy to parse, and ready for use in downstream applications.
  - _Example (JSON):_
    ```json
    {
      "name": "Anas",
      "age": 22,
      "email": "anas@email.com"
    }
    ```

---

#### Use Cases for Structured Output

Structuring the output is crucial for building reliable applications on top of LLMs. Key use cases include:

- **API Calls:** Extracting parameters from user input to call a function or an external API.
- **Data Extraction:** Pulling specific pieces of information from a large block of text (e.g., extracting invoice details from a PDF).
- **Database Operations:** Converting natural language queries into structured data that can be inserted into a database.
- **Chain of Thought Reasoning:** Forcing the model to output its reasoning steps _and_ a final answer in separate, well-defined fields.
- **UI Generation:** Generating structured data that can be directly used to render components in a user interface.

---

#### How It Works: Behind the Scenes

The `.with_structured_output()` method isn't magic. Under the hood, **LangChain modifies the prompt sent to the LLM**. It inspects the schema you provide (whether it's Pydantic, `TypedDict`, or JSON Schema) and appends detailed instructions to the prompt.

These instructions tell the model:

1.  Exactly what format to use for its response.
2.  The names of the fields (`name`, `age`).
3.  The data types for each field (`string`, `integer`).
4.  Any descriptions or constraints provided in the schema.

This makes it much more likely that the model will return the data in the exact structure you need.

---

#### Types of Schema Definitions

You can define your desired output structure in several ways. Let's explore the most common ones.

#### 1. `TypedDict`

A `TypedDict` is a standard Python feature for defining dictionary shapes with type hints. It's simple and requires no external libraries.

- **How it works:** You define a dictionary structure, and you can use docstrings to provide descriptions for the model.
- **Limitation:** `TypedDict` is for **static type checking only**. It offers **no runtime validation**. If the LLM returns an age as a string (`"32"`) instead of an integer (`32`), `TypedDict` will not automatically convert or validate it.

#### 2. Pydantic

**Pydantic** is the recommended and most powerful way to define schemas in LangChain. It's a data validation library that provides many features out of the box.

- **Key Features:**
  - **Type Coercion:** Automatically converts data to the correct type (e.g., a string `"42"` becomes an integer `42`).
  - **Built-in Validation:** Provides powerful validators for common types like emails, URLs, and more. If the LLM returns an invalid email, Pydantic will raise a validation error.
  - **Detailed Descriptions:** You can use the `Field` function from Pydantic to provide rich descriptions and constraints for each attribute, which are passed to the LLM in the prompt.

#### 3. JSON Schema

JSON Schema is a language-agnostic standard for defining the structure of JSON data.

- **When to use:**
  - When you need to interoperate with systems outside the Python ecosystem (e.g., a JavaScript frontend).
  - When you already have a predefined JSON Schema from an external source or API specification.
- **What to include:** The schema is a dictionary that defines the `type` of the object (usually `"object"`), the `properties` (fields), and which properties are `required`.

---

#### What to Use and When?

| Method          | Best For                                                                       | Pros                                                          | Cons                                              |
| --------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------- |
| **`TypedDict`** | Quick, simple data structures without needing validation. Prototyping.         | - No external dependencies<br>- Simple syntax                 | - **No runtime validation**<br>- No type coercion |
| **Pydantic**    | **The default choice for most Python applications.**                           | - Robust validation<br>- Type coercion<br>- Rich descriptions | - Requires installing `pydantic`                  |
| **JSON Schema** | Interoperability with non-Python systems or using existing schema definitions. | - Language-agnostic<br>- Standardized format                  | - More verbose to write<br>- Less Pythonic        |

---

#### The `method` Parameter

The `.with_structured_output()` function has a `method` parameter that controls _how_ the formatting instructions are passed to the LLM.

- **`method="function_calling"` or `"tool_calling"` (Default & Recommended):** This uses the model's native function/tool calling capabilities. It's generally the most reliable method for models that support it (like OpenAI, Gemini, Anthropic).
- **`method="json_mode"`:** This uses a model's dedicated JSON output mode. It's a good option for models that have this feature but might be less flexible than tool calling.
- **`method="json_tool"`:** This is a fallback that wraps your schema in a generic "json_tool", useful for models that don't explicitly support the other methods.

You can specify it like this:

```python
# Forcing the use of JSON mode if supported by the model
structured_llm = llm.with_structured_output(
    UserInfo,
    method="json_mode"
)
```

For most modern models, the default (`"tool_calling"`) is the best choice and you don't need to specify it.

---

#### Conclusion

Using `.with_structured_output()` is a fundamental technique for building reliable, production-grade applications with LangChain. By defining a clear schema, you transform the unpredictable nature of LLMs into a predictable and parsable data source.

- Start with **Pydantic** for its powerful validation and ease of use.
- Use `TypedDict` for very simple, internal scripts where validation is not a concern.
- Use JSON Schema when you need to share your data structure definitions across different platforms or languages.

---

Made with ❤️ by Mohd Anas Khan
