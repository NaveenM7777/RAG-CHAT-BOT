from langchain_groq import ChatGroq
from config import GROQ_API_KEY


def get_llm():

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.7,
        api_key=GROQ_API_KEY
    )

    return llm