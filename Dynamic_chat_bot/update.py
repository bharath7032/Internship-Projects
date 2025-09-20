import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# Load documents from "docs" folder
def load_documents():
    documents = []
    docs_dir = "docs"

    for file in os.listdir(docs_dir):
        filepath = os.path.join(docs_dir, file)
        if file.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
            documents.extend(loader.load())
        elif file.endswith(".docx"):
            loader = Docx2txtLoader(filepath)
            documents.extend(loader.load())
        else:
            print(f"Skipping unsupported file: {file}")
    return documents


# Create FAISS vector store
def create_vector_store():
    documents = load_documents()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local("faiss_index")
    print("✅ Vector store created and saved as 'faiss_index'")


if __name__ == "__main__":
    create_vector_store()
