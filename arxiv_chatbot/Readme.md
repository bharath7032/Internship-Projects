ArXiv Expert Chatbot

A beginner-friendly chatbot that lets you search research papers, read summaries, and get simple explanations from ArXiv data.
It also includes a small ML model (trained with scikit-learn) that classifies papers into categories.

Features

Search papers by topic (e.g., neural networks, reinforcement learning).

View paper title, authors, abstract.

ML Model: Classifies papers into categories.

Easy-to-use Streamlit UI.

Project Structure
arxiv_chatbot/
│── app.py                # Streamlit chatbot app
│── train_model.ipynb     # Notebook to train & save ML model
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── data/
│   └── arxiv_30.json     # Sample dataset (small subset of papers)
│── models/
│   ├── paper_classifier.pkl   # Saved ML model
│   └── vectorizer.pkl         # Saved text vectorizer

Installation

Clone the repo (or download the folder).

git clone https://github.com/yourusername/arxiv-chatbot.git
cd arxiv-chatbot


Install dependencies

pip install -r requirements.txt


Run Streamlit app

streamlit run app.py

Training the Model

If you want to retrain:

Open train_model.ipynb in Jupyter Notebook.

Run all cells (it will create models/paper_classifier.pkl and models/vectorizer.pkl).

These files will be used automatically by app.py.

Usage

Run the chatbot:

streamlit run app.py


Enter a topic (e.g., transformers).

The chatbot will:

Show relevant papers from dataset.

Display summaries in simple terms.

Predict the paper category.

Tech Stack

Python 3.x

Streamlit (UI)

scikit-learn (ML model)

Pickle (save/load model)

JSON dataset

Example
Input:

neural networks


Output:

Title: Deep Learning with Neural Nets

Authors: A. Researcher, B. Scientist

Abstract: ...

Category (predicted): Computer Science → Machine Learning

Summary (simplified): This paper explains how neural networks learn patterns from data.