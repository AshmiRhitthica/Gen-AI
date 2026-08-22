# LangChain Tool Calling Agent

A simple **Generative AI agent built with LangChain** that demonstrates how an LLM can use custom Python tools to perform tasks based on the user's query.

This project explores the basic workflow of creating an agent, defining tools, connecting them to an LLM, and allowing the agent to decide when a tool is needed.

## Overview

The project uses:

* **LangChain** for agent orchestration
* **Google Gemini** as the LLM
* **Custom Python tools** for specific tasks
* **LangChain `create_agent()`** to create the agent
* **Tool calling** to allow the LLM to invoke the appropriate function

## Tools Implemented

### 1. Word Count

The `get_word_count()` tool counts the number of words in the provided text.

```python
@tool
def get_word_count(text: str) -> str:
    """Count the number of words in the given text."""
    return f"{len(text.split())} words"
```

Example:

```text
Input:
How many words are in 'Hello world this is LangChain'?

Output:
5 words
```

### 2. Reverse Text

The `reverse_text()` tool reverses the given text.

```python
@tool
def reverse_text(text: str) -> str:
    """Reverse the given text."""
    return text[::-1]
```

Example:

```text
Input:
Reverse "Hello World"

Output:
dlroW olleH
```

## Agent Workflow

```text
User Query
     ↓
   Gemini LLM
     ↓
Agent decides whether a tool is required
     ↓
 ┌───────────────┐
 │               │
 ↓               ↓
Word Count    Reverse Text
 │               │
 └───────┬───────┘
         ↓
      Tool Result
         ↓
     Final Response
```

## Implementation

The tools are registered with the agent:

```python
tools = [reverse_text, get_word_count]

agent = create_agent(llm, tools)
```

The agent can then process user messages:

```python
response = agent.invoke({
    "messages": [
        ("user", "How many words are in 'Hello world this is LangChain'?")
    ]
})
```

The final response can be accessed using:

```python
response["messages"][-1].content
```

## Example Queries

The agent can handle queries such as:

```text
How many words are in "Hello world this is LangChain"?

Reverse the text "Generative AI"
```

It can also answer general questions that don't require the custom tools, for example:

```text
Explain Machine Learning.
```

This demonstrates the difference between **tool-based tasks** and **general LLM responses**.

## Key Concepts Learned

* Creating custom tools using LangChain's `@tool`
* Providing type hints and tool descriptions
* Registering tools with an agent
* Creating an agent using `create_agent()`
* Connecting Gemini with LangChain
* Agent-based tool selection
* Invoking an agent with messages
* Accessing the final agent response

## Requirements

Install the required packages:

```bash
pip install langchain langchain-google-genai
```

## API Key

The Gemini API key should **not be hardcoded** in the source code.

A safer approach is to store it as an environment variable


## Purpose

This is a learning implementation created while exploring **LangChain agents and tool calling**.

The project focuses on understanding the core agent workflow before moving toward more complex applications such as multi-tool agents, conversational agents, and multi-agent systems.
