from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from document_loader import load_pdf
from text_splitter import split_documents
from embeddings import get_embedding_model
from vector_store import create_vector_store
from retriever import create_retriever
from llm import get_llm


class RAGState(TypedDict):
    question: str
    context: str
    answer: str


def create_rag_pipeline(pdf_path):

    # Load and process documents
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)

    # Create vector store and retriever
    embedding_model = get_embedding_model()
    vector_store = create_vector_store(chunks, embedding_model)
    retriever = create_retriever(vector_store)

    # Initialize LLM
    llm = get_llm()

    # Node 1: Retrieve relevant documents
    def retrieve(state: RAGState):
        docs = retriever.invoke(state["question"])

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        return {"context": context}

    # Node 2: Generate answer
    def generate(state: RAGState):
        prompt = f"""
        Answer the question using the given context.
        If the answer is not available in the context,
        say you don't know.

        Context:
        {state["context"]}

        Question:
        {state["question"]}
        """

        response = llm.invoke(prompt)

        return {"answer": response.content}

    # Build LangGraph workflow
    graph = StateGraph(RAGState)

    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)

    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    rag_app = graph.compile()

    return rag_app