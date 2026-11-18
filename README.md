# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions based on their content.

## Features

- Upload PDF documents.
- Extract text from PDFs using PyMuPDF.
- Split documents into smaller chunks using LangChain.
- Generate embeddings using Sentence Transformers.
- Store and search embeddings using FAISS.
- Retrieve the top 3 relevant chunks.
- Generate answers using Groq LLM.
- Manage the RAG workflow using LangGraph.
- Interactive interface built with Streamlit.

## Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- PyMuPDF
- Sentence Transformers
- FAISS
- Groq LLM

## Project Structure

```text
RAG-CHAT-BOT/
├── app.py
├── config.py
├── document_loader.py
├── text_splitter.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── llm.py
├── rag_pipeline.py
├── requirements.txt
├── .env
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/NaveenM7777/RAG-CHAT-BOT.git
cd RAG-CHAT-BOT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your actual Groq API key.

### 6. Run the application

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the extracted text into chunks.
4. Convert chunks into vector embeddings.
5. Store embeddings in FAISS.
6. Retrieve the top 3 relevant chunks based on the user's question.
7. Pass the retrieved context and question to the Groq LLM.
8. Generate and display the answer.

## Author

Naveen