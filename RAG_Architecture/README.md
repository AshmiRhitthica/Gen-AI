# RAG Architecture

A simple **Retrieval-Augmented Generation (RAG)** implementation that combines document retrieval with a Large Language Model to generate answers based on relevant information from a knowledge base.

## Workflow

1. **Document Loading** – Loads the source text from a document.
2. **Text Normalization** – Cleans and prepares the text.
3. **Tokenization** – Processes the text using NLP techniques.
4. **Chunking** – Splits the document into smaller overlapping chunks.
5. **Embeddings** – Converts text chunks into numerical vector representations.
6. **Vector Database** – Stores the embeddings using FAISS.
7. **Similarity Search** – Retrieves the most relevant chunks for a user query.
8. **Generation** – Sends the retrieved context and query to Google Gemini to generate the final answer.

## Technologies Used

* Python
* LangChain
* Hugging Face Embeddings
* FAISS
* spaCy
* TextBlob
* Google Gemini
* Regular Expressions

## Purpose

This project demonstrates the basic architecture of a RAG system and how **retrieval and generation work together** to provide context-based responses.

## Files

* `RAG_architecture.ipynb` — RAG implementation and experiments
* `data.txt` — Knowledge base used for retrieval

## Future Improvements

* Improve document preprocessing
* Experiment with different embedding models
* Compare different chunking strategies
* Add conversation history
* Improve retrieval accuracy
* Build a user interface for the RAG system
