#Dynamic Knowledge Base Chatbot

#Project Overview
This project implements a chatbot with a **dynamically expandable knowledge base** using **LangChain, FAISS, and OpenAI embeddings**.  
It also includes a simple **text classification ML model** (trained in `model_training.ipynb`) to meet internship requirements.

#Folder Structure
- `app.py` → Streamlit chatbot app  
- `update.py` → Auto-updater for knowledge base  
- `requirements.txt` → Dependencies  
- `model_training.ipynb` → Jupyter Notebook (text classification, accuracy ≥70%)  
- `saved_model/` → Trained ML model + vectorizer  
- `data/` → Initial knowledge base  
- `new_data/` → New documents (auto-added to DB)  
- `report.pdf` → Internship report  

#How to Run
1. Install requirements:
   ```bash
   pip install -r requirements.txt

