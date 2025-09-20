<<<<<<< HEAD
🩺 MedQuAD Medical Q&A Chatbot
Overview

This project builds a medical question-answering chatbot using the MedQuAD dataset.
It retrieves the most relevant medical answers to user questions using TF-IDF + Cosine Similarity and provides a simple Streamlit interface.

📂 Project Structure
medquad_qa_chatbot/
├── app.py                 # Streamlit chatbot app
├── train_medquad.ipynb    # Jupyter Notebook for training & preprocessing
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── data/
    └── MedQuAD-master/    # MedQuAD dataset (download separately)

NOTE: Due to oversize of the dataset it is uploaded separately. you can check it  in the repository as data
    

⚙️ Setup

Clone this repo or create the project folder:

cd C:\Users\sbhar\projects\medquad_qa_chatbot

Download MedQuAD dataset from GitHub

→ Place it inside:

data/MedQuAD-master/


Install dependencies:

pip install -r requirements.txt


Run training notebook (train_medquad.ipynb) to:

Parse XML dataset

Save clean medquad_qa.csv

Start chatbot:

streamlit run app.py

🏆 Features

Retrieves top answers for user medical questions

Uses TF-IDF + Cosine Similarity for retrieval

Beginner-friendly code with simple structure

Interactive Streamlit interface

💬 Example Questions

What are the symptoms of diabetes?
How can asthma be treated?
What causes high blood pressure?
What is leukemia?
What are the side effects of chemotherapy?
=======
