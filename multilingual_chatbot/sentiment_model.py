# sentiment_model.py
from textblob import TextBlob

def predict_sentiment(text):
    """Return sentiment polarity and label for given text"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😀"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"
