# RAG Architecture – Retrieval and Evaluation

This project implements the **retrieval part of a Retrieval-Augmented Generation (RAG) architecture**, along with basic retrieval evaluation.

The workflow takes a text document, preprocesses it, splits it into chunks, converts the chunks into embeddings, stores them in a FAISS vector database, retrieves relevant chunks for a user query, and evaluates the retrieval results using standard retrieval metrics.

---

## Workflow

```text
Text Document
     ↓
Text Normalization
     ↓
Lemmatization + Stop-word Removal
     ↓
Chunking
     ↓
Chunk Embeddings
     ↓
FAISS Vector Database
     ↓
Similarity Search
     ↓
Retrieved Chunks
     ↓
Retrieval Evaluation
```

---

## 1. Document Loading

The input document is loaded from a `.txt` file.

---

## 2. Text Normalization

The document is normalized before creating chunks.

The preprocessing includes:

* Converting characters to lowercase
* Removing extra spaces
* Expanding contractions
* Removing punctuation and special characters
* Correcting words using `TextBlob`

---

## 3. Tokenization and Lemmatization

spaCy is used for tokenization and lemmatization.

Stop words are removed during preprocessing.

Words are converted into their lemma forms while removing stop words.

---

## 4. Chunking

The processed document is divided into smaller chunks using `RecursiveCharacterTextSplitter`.

### Chunk Configuration

| Parameter     | Value |
| ------------- | ----: |
| Chunk Size    |   200 |
| Chunk Overlap |    40 |

Metadata is also added to the first chunk:


---

## 5. Chunk Embeddings

Each chunk is converted into a vector representation using a Hugging Face sentence-transformer model.

The embeddings allow the text chunks to be compared based on semantic similarity.

---

## 6. Vector Database

FAISS is used as the vector database.

The processed chunks are stored in FAISS along with their embeddings.

---

## 7. Retrieval

A ground-truth set of relevant chunks is defined for the query.

The query is then used to retrieve similar chunks from FAISS.

The retrieved chunks are then compared against the manually defined relevant chunks.

---

# 8. Retrieval Evaluation

The retrieval results are evaluated using four metrics:

* Recall@K
* Precision@K
* Reciprocal Rank
* Hit Rate

These metrics help measure how effectively the retrieval system returns relevant chunks.

---

## Recall@K

Recall@K measures how many of the relevant chunks were retrieved within the top `K` results.

---

## Precision@K

Precision@K measures how many of the retrieved top `K` results are relevant.

---

## Reciprocal Rank

Reciprocal Rank measures the position of the **first relevant retrieved chunk**.

A relevant result at rank 1 gives a score of `1.0`, rank 2 gives `0.5`, rank 3 gives `0.33`, and so on.

---

## Hit Rate

Hit Rate checks whether at least one relevant chunk was retrieved.

* `1.0` → at least one relevant chunk was retrieved
* `0.0` → no relevant chunk was retrieved

---

## Retrieval Evaluation Summary

| Metric          | What it measures                                     |
| --------------- | ---------------------------------------------------- |
| Recall@K        | How many relevant chunks were retrieved in the top K |
| Precision@K     | How many top-K retrieved chunks were relevant        |
| Reciprocal Rank | Position of the first relevant result                |
| Hit Rate        | Whether at least one relevant result was retrieved   |

---

## Technologies Used

* **Python**
* **LangChain**
* **FAISS**
* **Hugging Face Sentence Transformers**
* **spaCy**
* **TextBlob**
* **Contractions**

---

## Key Learning

This implementation helped me understand that building a RAG system is not only about generating an answer with an LLM. The **retrieval stage needs to be evaluated separately** to determine whether the system is actually retrieving the relevant information needed for generation.

The current implementation focuses on **document preprocessing, chunking, vector retrieval, and retrieval evaluation**.
