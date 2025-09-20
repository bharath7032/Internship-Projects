import joblib
import os

# Load trained model
model_path = os.path.join("models", "sentiment_model.joblib")
model = joblib.load(model_path)

# Predict function
def predict_sentiment(text):
    pred = model.predict([text])[0]
    if pred == 2:
        return "positive"
    elif pred == 1:
        return "neutral"
    else:
        return "negative"
