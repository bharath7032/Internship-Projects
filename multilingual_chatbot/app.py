import streamlit as st
from langdetect import detect
from googletrans import Translator
from sentiment_model import predict_sentiment

translator = Translator()

# Base responses
base_responses = {
    "positive": "😊 I'm glad to hear that! How else can I assist you?",
    "negative": "😟 I'm sorry to hear that. Let me help you resolve this.",
    "neutral":  "😐 I understand. Could you tell me more?"
}

# Manual language overrides for short phrases
overrides = {"namaskaram": "te", "ela unnaru": "te", "namaste": "hi", "hola": "es", "bonjour": "fr"}

def get_response(text):
    lang = detect(text)
    for phrase, l in overrides.items():
        if phrase.lower() in text.lower():
            lang = l
            break
    sentiment = predict_sentiment(translator.translate(text, src=lang, dest="en").text) if lang != "en" else predict_sentiment(text)
    sentiment = sentiment if sentiment in base_responses else "neutral"
    response = translator.translate(base_responses[sentiment], src="en", dest=lang).text if lang != "en" else base_responses[sentiment]
    return response, lang, sentiment

st.title("🌍 Multilingual Sentiment-Aware Chatbot")
st.write("Type in ANY language; I'll detect it, analyze sentiment, and respond in your language!")

user_input = st.text_input("You:")
if user_input:
    response, detected_lang, sentiment = get_response(user_input)
    st.write(f"📝 Detected language: {detected_lang} | 📊 Sentiment: {sentiment}")
    st.write("🤖 Bot:", response)
