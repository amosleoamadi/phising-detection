# Phishing Detection System

A machine learning-powered phishing detection system built with FastAPI that detects suspicious text messages and malicious URLs.

The system analyzes user input and classifies it as either:

- Phishing
- Safe

This project combines Natural Language Processing (NLP), URL feature extraction, and machine learning models to improve phishing detection accuracy.

---

# Features

- Detect phishing text messages
- Detect malicious URLs
- FastAPI REST API
- Machine learning integration
- TF-IDF text classification
- URL feature extraction
- Frontend integration support
- CORS enabled
- Swagger API documentation

---

# Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Machine Learning

- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer
- DictVectorizer
- NLTK

## Data Processing

- Pandas
- Regex
- Joblib

---

# Project Structure

```bash
app/
│
├── main.py
│
├── routes/
│   └── predictor.py
│
├── services/
│   ├── prediction_service.py
│   ├── predict_text.py
│   └── predict_url.py
│
├── utils/
│   ├── helpers.py
│   └── url_features.py
│
├── schemas/
│   └── predict_schema.py
│
├── models/
│   ├── text_model.pkl
│   ├── text_vectorizer.pkl
│   ├── url_model.pkl
│   └── url_vectorizer.pkl
│
├── dataset/
│   ├── spam.csv
│   └── Dataset.csv
│
├── train_model.py
├── train_url_model.py
│
└── requirements.txt
```
