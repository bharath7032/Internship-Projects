# Multi-Modal Chatbot with Google Gemini

##Project Overview
This project implements a **multi-modal chatbot** using **Google Gemini AI**.  
The chatbot can:
- Understand and respond to text queries
- Analyze uploaded images and answer questions about them
- Generate new images from text prompts  

The goal is to extend a chatbot beyond text, enabling it to seamlessly integrate **visual + textual understanding**.

## Project Structure
multimodal_chatbot/
├── app.py # Streamlit app
├── requirements.txt # Dependencies
├── .env # Store your Google API Key (not committed to Git)
└── README.md # Project documentation

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/multimodal_chatbot.git
cd multimodal_chatbot
2. Create Virtual Environment (recommended)

conda create -n mmchat python=3.10 -y
conda activate mmchat
3. Install Dependencies

pip install -r requirements.txt
4. Add API Key
Create a .env file in the project folder and add:

Copy code
GOOGLE_API_KEY=your_api_key_here
You can get an API key from Google AI Studio.

5. Run App

python -m streamlit run app.py
Then open in your browser: http://localhost:8501

Features
Chat Mode (Text): Send text queries and get intelligent responses

Image Analysis Mode: Upload an image and ask the bot questions about it

Image Generation Mode: Provide a description and generate an image

Evaluation
The project does not involve training a custom ML model.
Instead, it leverages Google Gemini’s pre-trained multi-modal intelligence.
Evaluation is based on:

Accuracy of Gemini’s responses

Correctness of image analysis

Quality of generated images

User experience of the chatbot

Requirements
Main dependencies:

streamlit

google-generativeai

python-dotenv

pillow

(see requirements.txt for full list)

