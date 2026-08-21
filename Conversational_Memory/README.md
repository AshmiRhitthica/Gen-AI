# Conversational Memory with Session Management

A hands-on Generative AI implementation demonstrating how to build **conversation memory with multiple independent sessions using LangChain**.

This project explores how an LLM can maintain conversation context across multiple interactions and keep the memory of different users/sessions separate.

---

## Project Overview

A normal LLM call treats each request independently unless previous conversation messages are provided again.

This implementation uses:

* **LangChain**
* **Google Gemini**
* **ChatPromptTemplate**
* **MessagesPlaceholder**
* **InMemoryChatMessageHistory**
* **RunnableWithMessageHistory**
* **Session IDs**

to maintain conversation history across multiple interactions.

---

## Architecture

```text
User Input
    ↓
Chat Function
    ↓
Session ID
    ↓
RunnableWithMessageHistory
    ↓
get_session_history()
    ↓
Session Store
    ↓
InMemoryChatMessageHistory
    ↓
Conversation History
    ↓
Prompt
    ↓
Gemini LLM
    ↓
Response
    ↓
Stored in Session History
```

---

## Features

### 1. Conversational Memory

The assistant remembers information provided earlier in the same session.

Example:

```text
User: My name is Ashmi.

AI: Nice to meet you, Ashmi!

User: What is my name?

AI: Your name is Ashmi.
```

The second query works because the previous conversation is available through the session history.

---

### 2. Multiple Sessions

Each conversation is identified using a unique `session_id`.

For example:

```python
chat("user_1", "My name is Ashmi.")
chat("user_2", "My name is Rithi.")
```

These conversations are stored separately.

```text
user_1
 ├── My name is Ashmi.
 └── What is my name?

user_2
 ├── My name is Rithi.
 └── What is my name?
```

Information from one session is not passed into another session.

---

## Session Store

A Python dictionary is used as the central store:

```python
store = {}
```

The `get_session_history()` function creates a new memory object when a session does not already exist.

```python
def get_session_history(session_id):

    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]
```

This allows each session to maintain its own conversation history.

---

## How Memory Is Connected

`RunnableWithMessageHistory` connects the conversation history with the LangChain chain.

```python
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)
```

The `session_id` determines which conversation history should be retrieved.

```python
config={
    "configurable": {
        "session_id": session_id
    }
}
```

---

## Testing

Two separate sessions are tested.

### Session 1

```python
chat("user_1", "My name is Ashmi.")
chat("user_1", "What is my name?")
```

Expected behavior:

```text
AI: ...
AI: Your name is Ashmi.
```

### Session 2

```python
chat("user_2", "My name is Rithi.")
chat("user_2", "What is my name?")
```

Expected behavior:

```text
AI: ...
AI: Your name is Rithi.
```

---

## Inspecting Stored Conversations

The project also prints the contents of the session store:

```python
for session_id, history in store.items():

    print("SESSION:", session_id)

    for message in history.messages:

        print(
            message.type,
            ":",
            message.content
        )
```

This makes it possible to see how the conversation is stored for each session.

Example:

```text
SESSION: user_1

human : My name is Ashmi.
ai : Nice to meet you, Ashmi!
human : What is my name?
ai : Your name is Ashmi.

SESSION: user_2

human : My name is Rithi.
ai : Nice to meet you, Rithi!
human : What is my name?
ai : Your name is Rithi.
```

---

## Environment Variable

The Gemini API key is **not hardcoded** in the source code.

The application reads it from an environment variable:

```python
os.environ["GOOGLE_GEMINI_API_KEY"]
```

Set the environment variable before running the project.

**Do not commit API keys or other secrets to GitHub.**

---

## Technologies Used

| Technology                 | Purpose                         |
| -------------------------- | ------------------------------- |
| Python                     | Implementation                  |
| LangChain                  | LLM application framework       |
| Google Gemini              | Language model                  |
| ChatPromptTemplate         | Prompt construction             |
| MessagesPlaceholder        | Inserting conversation history  |
| InMemoryChatMessageHistory | Storing conversation messages   |
| RunnableWithMessageHistory | Connecting sessions with memory |

---

## Key Concepts Learned

* LLM conversation memory
* Session-based memory
* Session IDs
* `InMemoryChatMessageHistory`
* `RunnableWithMessageHistory`
* `MessagesPlaceholder`
* LangChain chains
* Managing multiple independent conversations
* Inspecting stored conversation history
* Using environment variables for API keys

---

## Future Improvements

Possible extensions for this implementation:

* Add a command-line chat interface
* Add persistent memory using a database
* Store conversations in Redis or another backend
* Build a Streamlit chat interface
* Add conversation summarization
* Add long-term user memory
* Integrate memory into a RAG application
* Replace in-memory storage with persistent session storage

---

## Purpose

This project is part of my hands-on learning journey in **Generative AI and LangChain**, focusing on understanding how conversational memory and session management work internally rather than treating memory as a black box.
