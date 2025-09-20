# app.py
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

st.title("Dynamic AI Chatbot")

# Load vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

user_input = st.text_input("Ask me anything:")

if st.button("Submit") and user_input:
    docs = db.similarity_search(user_input, k=2)
    answer = " ".join([d.page_content for d in docs])
    st.write(answer)
