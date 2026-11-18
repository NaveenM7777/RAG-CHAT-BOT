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

if uploaded_file is not None:

    with open("uploaded_document.pdf", "wb") as file:
        file.write(uploaded_file.getbuffer())

    rag_app = create_rag_pipeline("uploaded_document.pdf")

    question = st.text_input("Ask your question")

    if st.button("Submit") and question:

        result = rag_app.invoke({
            "question": question,
            "context": "",
            "answer": ""
        })

        st.write("### Answer")
        st.write(result["answer"])