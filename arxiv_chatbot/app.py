import streamlit as st
import json
import random

# --------------------------
# Load dataset
# --------------------------
def load_data():
    with open("data/arxiv_30.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

papers = load_data()

# --------------------------
# Simple Search Function
# --------------------------
def search_papers(query, papers):
    results = []
    for paper in papers:
        if query.lower() in paper["title"].lower() or query.lower() in paper["summary"].lower():
            results.append(paper)
    return results

# --------------------------
# Streamlit App
# --------------------------
st.set_page_config(page_title="ArXiv Chatbot", page_icon="📚")
st.title("📚 ArXiv Expert Chatbot (Beginner Friendly)")

st.write("Search papers, read summaries, and get simple explanations.")

# User input
query = st.text_input("🔍 Enter a topic (example: neural networks, reinforcement learning):")

if query:
    results = search_papers(query, papers)

    if results:
        st.subheader("Search Results:")
        for paper in results:
                with st.expander(paper["title"]):
                    st.write(f"**Authors:** {', '.join(paper.get('authors', []))}")
                    st.write(f"**Abstract:** {paper['summary']}")
                    st.write(f"**URL:** {paper.get('url', 'No link available')}")

            

                # Simple explanation (dummy beginner-friendly explanation)
                if st.button(f"Explain in simple terms: {paper['title']}", key=paper["id"]):
                    st.info("This paper is about " + random.choice([
                        "using AI to solve problems in computer science.",
                        "applying machine learning to improve predictions.",
                        "exploring deep learning methods for research.",
                        "studying advanced concepts but can be understood as improving computers' thinking."
                    ]))
    else:
        st.warning("No papers found for your search.")
else:
    st.write("👆 Enter a keyword to search papers.")
