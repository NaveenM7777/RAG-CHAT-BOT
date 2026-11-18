import streamlit as st
from rag_pipeline import create_rag_pipeline

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖"
)

st.title("📚 RAG Chatbot")
st.write("Ask questions based on your PDF document.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

@st.cache_resource
def load_rag_pipeline(pdf_path):
    return create_rag_pipeline(pdf_path)

if uploaded_file is not None:

    with open("uploaded_document.pdf", "wb") as file:
        file.write(uploaded_file.getbuffer())

    with st.spinner("Processing PDF and creating RAG pipeline..."):
        rag_app = load_rag_pipeline("uploaded_document.pdf")

    st.success("PDF processed successfully!")

    question = st.text_input("Ask your question")

    if st.button("Submit") and question:

        with st.spinner("Generating answer..."):
            result = rag_app.invoke({
                "question": question,
                "context": "",
                "answer": ""
            })

        st.write("### Answer")
        st.write(result["answer"])