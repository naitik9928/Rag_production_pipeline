# 🤖 RAG Q/A System - Document Intelligence API

An end-to-end, production-ready Retrieval-Augmented Generation (RAG) system designed to extract intelligence from private PDF documents. The system seamlessly ingests PDF files, vectorizes text chunks, handles semantic similarity retrieval via an on-disk vector store, and serves contextual, lightning-fast answers using Groq's high-performance **Llama 3.3 70B** model via a structured FastAPI REST API.

---

## 🚀 Features

* **Asynchronous Ingestion Pipeline:** Automated ingestion of multi-page PDFs with text extraction and tracking.
* **Optimized Text Chunking:** Smart recursive character splitting with tuned token overlap to preserve contextual continuity.
* **Local Embeddings generation:** Uses the lightweight yet powerful `all-MiniLM-L6-v2` HuggingFace transformer model to keep embedding calculations zero-cost.
* **Persistent Storage:** Native disk-based vector storage using ChromaDB to enable swift semantic similarity queries without re-indexing.
* **Enterprise-Grade LLM Orchestration:** Powered by LangChain and Groq API cloud compute using the state-of-the-art `llama-3.3-70b-versatile` engine.
* **Production API Layer:** Fully typed request/response handling with Pydantic validations, OpenAPI interactive docs, and automatic daily rolling log files.
* **Containerized Architecture:** Fully dockerized workspace layout to enable consistent deployment across local machines or cloud servers.

---

## 📁 Project Structure

```text
rag-qa-system/
│
├── app.py                  # FastAPI server and routing layer
├── rag_engine.py           # Core RAG logic and LangChain orchestration
├── ingested.py             # Data ingestion pipeline & vector store builder
├── logger.py               # Centralized rolling file log configuration
├── requirements.txt        # Documented Python dependencies
├── Dockerfile              # Containerization recipe
├── .gitignore              # Keeps databases and secrets out of version control
│
├── docs/                   # 📁 Drop your target source PDFs here
│   └── sample_policy.pdf    
│
├── chroma_database/        # Local persistent vector database (Auto-generated)
└── logs/                   # System operational tracing log directory (Auto-generated)


## 🛠️ Quick Start Guide

### 1. Prerequisites & Environment Setup

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

# Install required modules
pip install -r requirements.txt
