# Gen-AI

A collection of my learning projects and implementations in **Machine Learning, Natural Language Processing, Generative AI, and Retrieval-Augmented Generation (RAG)**.

## Projects

### Text Normalization

A Python-based text normalization implementation covering:

* Lowercase conversion
* Punctuation and special character handling
* Emoji handling
* Contraction expansion
* Repeated character normalization
* Extra space removal
* Spell correction

### RAG Architecture

A Retrieval-Augmented Generation project demonstrating:

* Text preprocessing
* Text chunking
* Embeddings
* FAISS vector database
* Similarity search
* Retrieval
* LLM-based response generation

### Retrieval Testing

A retrieval evaluation implementation for the RAG architecture covering:

* Retrieval ground truth creation
* Similarity-based retrieval using FAISS
* Recall@K
* Precision@K
* Reciprocal Rank
* Hit Rate
* Evaluation of retrieved chunks against relevant chunks

### Conversational Memory

A conversational AI implementation demonstrating session-based chat memory using LangChain.

The project covers:

* Chat prompt creation
* Gemini LLM integration
* Conversation history management
* Session-based memory
* InMemoryChatMessageHistory
* RunnableWithMessageHistory
* Maintaining separate conversations using session IDs
* Testing multiple user sessions
* Inspecting stored conversation history

### LangChain Tool Calling Agent

A simple AI agent implementation using LangChain and Google Gemini, demonstrating how an LLM can use custom Python tools based on the user's query.

The project covers:

* Creating custom tools using LangChain's `@tool`
* Building a word-count tool
* Building a text-reversal tool
* Connecting Google Gemini with LangChain
* Creating an agent using `create_agent`
* Agent-based tool selection
* Invoking an agent with user messages
* Handling tool-based tasks and general LLM questions
* Accessing the final agent response

## 📌About This Repository

This repository documents my hands-on learning and implementation of concepts in **AI and Generative AI** through practical projects.

Each project focuses on understanding a specific concept by implementing it with Python and relevant AI frameworks.

More projects and implementations will be added as I continue learning.


