# predict_url.py (already yours, just ensure imports are correct)
import joblib
from app.utils.url_features import extract_url_features

model = joblib.load("models/url_model.pkl")
vectorizer = joblib.load("models/url_vectorizer.pkl")

def predict_url(url: str):
    features = extract_url_features(url)
    X = vectorizer.transform([features])
    pred = model.predict(X)[0]
    return "phishing" if pred == 1 else "safe"

# Test
print(predict_url("http://hshhdy.vuuu"))   # should be "phishing"
print(predict_url("https://google.com"))   # should be "safe"