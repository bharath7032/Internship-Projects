Multilingual Sentiment-Aware Chatbot
Overview

This project is a multilingual chatbot that:

Detects the language of user input automatically.

Analyzes the sentiment (positive, negative, neutral).

Responds in the same language as the user.

Supports multiple languages, including short phrases and greetings.

The chatbot is built using Streamlit, FastText for language detection, Google Translate API for translation, and TextBlob-based sentiment analysis.

Project Structure
multilingual_chatbot/
│── app.py
│── requirements.txt
│── README.md
│
├── sentiment_model.py
├── models/
│   └── lid.176.bin   # FastText language detection model
└── notebooks/
    └── train_sentiment_model.ipynb

Installation & Setup

Clone the repository:

git clone <your-github-repo-link>
cd multilingual_chatbot


Create a virtual environment (recommended):

conda create -n chatbot_env python=3.10 -y
conda activate chatbot_env


Install required packages:

pip install -r requirements.txt


requirements.txt should include:

streamlit
googletrans==4.0.0-rc1
textblob
fasttext


Download FastText language detection model (lid.176.bin) and save it in models/.

Running the Chatbot

Run the Streamlit app:

streamlit run app.py


Open the local URL in your browser (usually http://localhost:8501) to chat with the bot.

How it works

User Input: Type any sentence or phrase in any language.

Language Detection: FastText automatically detects the language.

Sentiment Analysis: Input is translated to English (if not English) for sentiment classification.

Response Generation: The bot selects a base response depending on sentiment.

Translation Back: Response is translated to the user’s language.

Display: Streamlit shows the detected language, sentiment, and bot response.

🔧 Features

Detects almost any language, including short phrases.

Supports positive, negative, neutral sentiment responses.

Provides responses in the same language as user input.

Beginner-friendly and easy to extend for more languages or intents.