import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🩺 Simple Medical Q&A Chatbot")

# Load dataset
df = pd.read_csv("data/medquad_qa.csv")

# Build retriever
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["question"])

def get_answer(user_q):
    sims = cosine_similarity(vectorizer.transform([user_q]), X)
    idx = sims.argmax()
    return df.iloc[idx]["answer"]

# User input
user_q = st.text_input("Ask a medical question:")

if st.button("Get Answer"):
    st.write(get_answer(user_q))
