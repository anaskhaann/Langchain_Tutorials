# Runnables in LangChain

Runnables provide a flexible, scalable way to build AI workflows, addressing limitations of earlier chain designs.**_Runnables_** are the building blocks of modern LangChain architecture—powerful, composable units (like models, parsers, retrievers, or even custom Python logic) that can be executed, inspected, or combined seamlessly.  
They generalize "chains" into a unified interface with support for invocation, batching, streaming, and composition via **LCEL (LangChain Expression Language).**

## Why We Need Runnables

Runnables enable production-ready AI applications by supporting low latency, scalability, and observability. They offer:

- Automatic parallel processing and async support.
- Streaming for incremental outputs.
- Integration with tools like LangSmith for tracing.

Before Runnables, LangChain users relied on specialized constructs like `Chain` classes (e.g., `LLMChain`), which made building flexible workflows somewhat rigid.

## Problems LangChain Solved and Where They Got Stuck

LangChain initially simplified LLM app development by integrating models, prompts, retrievers, and parsers into reusable chains, reducing boilerplate code for memory, agents, and data retrieval.

- Standardized how components like prompts, models, and parsers interact.
- Allowed advanced behaviors like streaming, batching, async executions, and schema inspection in a unified way.

These limitations hindered scalability and debugging, especially as LLM diversity grew.

- Chains were inflexible and didn’t support composition or introspection uniformly.
- As applications grew complex (branching, parallelism), the chain model didn’t scale well.

## How They Created Chains and Transitioned to Runnables

LangChain originally had constructs like `LLMChain`, but as workflows became more dynamic, users needed powerful abstractions.  
This led to the creation of **Runnables**—a uniform interface for any component—and the development of **LCEL** and various Runnable types to better manage flow, branching, and concurrency.

LangChain started with specialized chains like LLMChain and ConversationalRetrievalChain, each tailored for specific tasks. This led to a complex ecosystem of chains that were hard to modify or extend, especially for streaming or parallel tasks. Around late 2023, LangChain introduced Runnables as a unified interface via the LangChain Expression Language (LCEL). Runnables replaced rigid chains with composable, transparent components, enabling declarative workflows without subclassing.

## What Are Runnables

Runnables are standardized LangChain components that implement a common interface for invocation, batching, and streaming. They represent executable units (e.g., LLMs, prompts, or custom functions) that can be composed into chains. Any LCEL-built chain is a Runnable, ensuring consistency across models, retrievers, and parsers.

## How Runnables Work

Runnables process inputs through methods like:

- Accepts input, emits output.
- `invoke`: For single inputs.
- `batch`: For multiple inputs.
- `stream`: For incremental outputs.
- Async variants (e.g., `ainvoke`).
- Exposes `input_schema` and `output_schema` for introspection.
- Can be composed using LCEL (using operators like `|`) to build complex pipelines.

They support configuration propagation (e.g., callbacks) and optimize for parallelism. You can inspect input/output schemas for clarity.

## Types of Runnables

Runnables are categorized as:

- **Task-Specific Runnables**: Pre-built for specific tasks, e.g., `ChatModel` for conversations, `Retriever` for data fetching, or `OutputParser` for formatting.
- **Runnable Primitives**: Foundational blocks for composition, including sequences, parallels, and conditionals, offering flexibility for custom pipelines.

## Runnable Sequence

A `RunnableSequence` executes components in order, passing each output as the next input. Ideal for linear workflows like prompt → model → parser.

```python
from langchain_core.runnables import RunnableSequence
sequence = prompt | model | parser  # LCEL syntax
output = sequence.invoke({"input": "Hello"})
```

## Runnable Parallel

`RunnableParallel` runs multiple Runnables simultaneously with the same input, returning a dictionary of results. Reduces latency for independent tasks.

```python
from langchain_core.runnables import RunnableParallel
parallel = RunnableParallel({"summary": summarizer, "details": detail_extractor})
output = parallel.invoke(input_data)  # Runs both in parallel
```

## Runnable Passthrough

`RunnablePassthrough` forwards input unchanged, often used to preserve context or assign inputs to keys in parallel workflows.

```python
from langchain_core.runnables import RunnablePassthrough
chain = RunnableParallel({"original": RunnablePassthrough(), "processed": processor})
output = chain.invoke(input_data)  # {"original": input_data, "processed": processed_result}
```

## Runnable Branch

`RunnableBranch` routes execution based on conditions, similar to if-else logic. It uses (condition, runnable) pairs and a default runnable.

```python
from langchain_core.runnables import RunnableBranch
branch = RunnableBranch(
    (lambda x: x["topic"] == "math", math_chain),
    default_chain
)
output = branch.invoke({"topic": "math"})
```

## Runnable Lambda

`RunnableLambda` wraps a Python function as a Runnable, enabling custom logic in chains. Useful for quick transformations.

```python
from langchain_core.runnables import RunnableLambda
custom = RunnableLambda(lambda x: x.upper())
output = custom.invoke("hello")  # "HELLO"
```

## LCEL (LangChain Expression Language)

LCEL is a declarative syntax using the pipe operator (`|`) to compose Runnables into sequences. It supports async, streaming, and parallelism, with automatic coercion (e.g., dicts to parallels). The `|` operator creates a `RunnableSequence`.

```python
chain = prompt | model | parser  # Composes sequence
output = chain.invoke(input_dict)
```

---

Made with ❤️ by **Mohd Anas**
