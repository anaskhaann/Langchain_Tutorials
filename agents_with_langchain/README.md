## **LangChain Agents**

While chains in LangChain follow a predetermined path, **Agents** introduce a world of autonomy. They are the components that can reason, make decisions, and dynamically choose a path to accomplish a goal, making them one of the most powerful concepts in the framework.

---

## What are Agents?

An **Agent** is an entity that uses an LLM not just to generate text, but as a **reasoning engine**. It is given a goal, a set of tools, and the autonomy to decide which tools to use—and in what sequence—to achieve that goal.

**Analogy**: If a LangChain chain is a factory assembly line with fixed, sequential steps, an agent is a skilled craftsman in a workshop. The craftsman has a goal (e.g., "build a chair") and a workbench full of tools (a saw, a hammer, sandpaper). They intelligently decide which tool to pick up at each step, observe the result, and plan their next move until the chair is complete.

#### Characteristics of an Agent

1. **Autonomous**: They can perform sequences of actions without requiring step-by-step human guidance.
2. **Goal-Oriented**: You provide a final objective, not a rigid set of instructions.
3. **Tool-Using**: Their primary way of interacting with the world is by using tools (e.g., search engines, calculators, APIs).
4. **Reasoning-Driven**: They leverage the power of an LLM to think, plan, and react to observations.

---

## `Agent` vs. `AgentExecutor`: Brain vs. Body

This is a critical distinction in LangChain. The "agent" system is made of two separate but essential parts:

1.  **The `Agent` (The Brain)**: This is the core logic, the "policy," or the decision-making engine. Its only job is to look at the user's input and the history of previous steps (`intermediate_steps`) and decide what to do next. It either outputs an `AgentAction` (which tool to use and with what input) or an `AgentFinish` (the final answer to the user). **Crucially, the `Agent` itself does not execute the tool.**

2.  **The `AgentExecutor` (The Body/Runtime)**: This is the runtime that actually makes the agent work. It's a loop that orchestrates the entire process.

#### How the `AgentExecutor` Works

The `AgentExecutor` is responsible for the loop that brings the agent to life:

1.  It receives the user input and sends it to the `Agent` (the brain).
2.  The `Agent` thinks and decides on an action (e.g., "use the search tool with the query 'latest AI news'").
3.  The `AgentExecutor` receives this action, takes the specified tool from the toolbox, and **executes it**.
4.  The result of the tool's execution (e.g., a list of search results) is called an **Observation**.
5.  The `AgentExecutor` takes this `Observation` and sends it back to the `Agent` along with the history of all previous steps.
6.  The loop repeats until the `Agent` decides it has enough information and outputs a final answer instead of an action.

---

## A Code Example

Here is how you would create and run a ReAct agent in practice.

#### Step 1: Creating the Agent (The Brain)

First, we assemble the components: the LLM, the tools, and a prompt template. The `create_react_agent` function bundles them into the agent runnable, which acts as the decision-making engine.

```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub

# Choose the LLM that will act as the agent's reasoning engine
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Define the set of tools the agent can use
tools = [DuckDuckGoSearchRun()]

# Pull the prompt template from the LangChain Hub
# This special prompt is designed to instruct the LLM on how to use tools
# and follow the ReAct (Reason-Act) framework.
prompt = hub.pull("hwchase17/react")

# Create the Agent runnable
agent = create_react_agent(llm, tools, prompt)
```

#### Step 2: Creating and Running the AgentExecutor (The Body)

Now, we take the `agent` runnable and pass it to the `AgentExecutor`, which will run the reasoning loop until the task is complete.

```python
from langchain.agents import AgentExecutor

# Create the AgentExecutor
# This is the runtime that powers the agent's loop.
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True  # Set to True to see the agent's step-by-step reasoning
)

# Run the AgentExecutor with a query
response = agent_executor.invoke({
    "input": "Who is the current Prime Minister of India and what is their age as of late 2025?"
})

# Print the final answer
print(response["output"])
```

---

## **The ReAct Agent**

**ReAct**, which stands for **Reasoning and Acting**, is the most famous and widely used agent architecture. It's a prompting strategy that explicitly tells the LLM to follow a specific thought process to solve problems.

#### The ReAct Architecture and Workflow

The ReAct framework forces the LLM to follow a specific cycle for each step: **Thought → Action → Observation**.

1.  **Thought**: The agent first thinks about the problem and writes down its reasoning. This internal monologue is crucial. It assesses the overall goal, what it knows so far, and what piece of information it needs next. (e.g., _Thought: I need to find the current weather in Mumbai. I should use a search tool._)
2.  **Action**: Based on its thought, the agent chooses a **Tool** and the **Input** for that tool. (e.g., _Action: Search(query="weather in Mumbai")_)
3.  **Observation**: The `AgentExecutor` runs the specified tool, and the result is returned as an `Observation`. (e.g., _Observation: "The current weather in Mumbai is 29°C with light rain."_)

This `(Thought, Action, Observation)` triplet is added to a "scratchpad" in the prompt, and the agent begins the next loop. It continues this process, building on its observations, until its thought process concludes that it can give a final answer.

#### When to Use a ReAct Agent

ReAct is an excellent general-purpose agent. It excels at tasks that require **multi-step reasoning**, where the next action depends on the result of the previous one. It's ideal for knowledge-intensive tasks like:

- Answering complex questions that require searching for and synthesizing information.
- Interacting with APIs where you need to make one call to get an ID, then another call using that ID.
- Debugging or performing "chain-of-thought" style reasoning where showing your work is important.

#### **ReAct Research Paper**

The concept was introduced in the paper: **"ReAct: Synergizing Reasoning and Acting in Language Models"**. You can read it on ArXiv: [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)

---

#### Some Other Types of Agent Architechture

1. **Simple Reflex Agents**: These agents act solely based on the current perception, using a set of condition-action rules. They have no memory of past states.

2. **Model-Based Reflex Agents**: These agents maintain an internal model of the environment, allowing them to track aspects not directly observable. They use this model, along with current perceptions, to make decisions.

3. **Goal-Based Agents**: These agents have a specific goal and plan their actions to achieve that goal. They consider the consequences of their actions to reach the desired state.

4. **Utility-Based Agents**: Extending goal-based agents, these agents evaluate actions based on a utility function, which quantifies the desirability of different states or outcomes. They aim to maximize their utility.

5. **Learning Agents**: These agents improve their performance over time through experience. They learn from feedback and adapt their behavior to optimize for better results.

6. **Hierarchical Agents**: These agents structure decision-making across multiple levels. Higher-level agents make strategic decisions and delegate specific tasks to lower-level agents.

7. **Multi-Agent Systems (MAS)**: These systems involve multiple autonomous agents that interact with each other, either cooperatively or competitively, to achieve individual or collective goals.

---

Made with ❤️ by **Mohd Anas**
