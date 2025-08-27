In this I am going to learn Generative AI with the help of Langchain.

Most of the notes will be handwritten and i will upload them later but each section will also contain a Small markdown which will demonstrate some parts which will be necessary.

## **Setup for the Code**

I am using UV for package management you can use pip also.

- run `uv init` or create venv manually
- `uv sync` to install required packages
- verify langchain by printing `print(langchain.__version__)`
- create `.env` and put all your API keys to it and add that to `.gitignore`
- You can also use `pip` and traditional method to create a virtual environment by running `python -m venv .venv`
- then Activate the environment by ` .venv\Scripts\Activate` for windows

---

## Outline

- [x] Models
  - Language Models | Embedding Models
  - Llm's and Chat Models
  - Parameters: temperature, token_size etc.
  - Open source models | Close source Models
- [x] Prompts
  - Types of Prompt
  - Single prompt , List of prompts(messages)
  - Static Prompt for Single prompt
  - Dynamic Prompt for Single Prompt
  - Prompt Template to make dynamic prompt
  - Basic Chatbot
  - Message History for chatbots
  - Labels for Message history: SystemMessage, HumanMessage, AIMessage.
  - Dynamic List of Messages(ChatPromptTemplate)
  - Message PlaceHolders
- [x] Structured Outputs
  - LLM which _is capable to structure output_ respose from text to defined data format.
  - Using Typed Dict : for checking
  - Using Pydantic : for validation
  - Using Json Schema : for cross programming workflow
- [x] Output Parser

  - LLM which do not have the capability to _structure the output_.
  - `StrOutputParser`: The simplest parser. It just passes the LLM's string output through without any changes.Ideal for chatbot responses or text summarization.
  - `JsonOutputParser`: Parses the LLM's output into a Python dictionary. It's useful for creating universally compatible JSON objects but offers no validation or type safety.
  - `StructuredOutputParser`: A step up from the JSON parser. You define a schema with field names and descriptions, which helps the LLM generate a more accurate dictionary. It still lacks validation.
  - `PydanticOutputParser`: The most powerful and recommended parser. It uses a Pydantic BaseModel to define the schema, providing automatic data validation, type coercion, and creating easy-to-use Python objects. This is the best choice for building reliable applications.

- [ ] Chains
- [ ] Memory
- [ ] Indexes
- [ ] Agents

---

Made with ❤️ by Mohd Anas Khan
