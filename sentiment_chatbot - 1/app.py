import streamlit as st
from sentiment_model import predict_sentiment

st.title("🌍 Multilingual Sentiment-Aware Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def chatbot_reply(user_msg):
    sentiment = predict_sentiment(user_msg)
    if sentiment == "positive":
        return "😊 I'm glad you’re happy! How can I assist you further?"
    elif sentiment == "neutral":
        return "😐 I understand. Could you tell me more?"
    else:
        return "😟 I'm sorry to hear that. Let me help you with your issue."

user_input = st.text_input("You:")
if st.button("Send"):
    st.session_state.messages.append(("You", user_input))
    reply = chatbot_reply(user_input)
    st.session_state.messages.append(("Bot", reply))

for role, msg in st.session_state.messages:
    st.write(f"**{role}:** {msg}")
