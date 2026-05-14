# app/predict_combined.py
import re
import joblib
import nltk
import string
from nltk.corpus import stopwords
from app.utils.url_features import extract_url_features   # your URL feature extractor

# Ensure NLTK data (run once)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# ---------- 1. Load both models ----------
# Text message model (spam/ham)
text_model = joblib.load("models/model.pkl")
text_vectorizer = joblib.load("models/vectorizer.pkl")

# URL model (phishing/safe)
url_model = joblib.load("models/url_model.pkl")
url_vectorizer = joblib.load("models/url_vectorizer.pkl")

# Stopwords for text cleaning
stop_words = set(stopwords.words("english"))

# ---------- 2. Text cleaning function (matches training) ----------
def cleaning_data(text: str) -> str:
    """Clean message exactly as done in training."""
    text = text.lower()
    # Replace URLs with placeholders
    urls = re.findall(r'https?://\S+|www\.\S+', text)
    for i, url in enumerate(urls):
        text = text.replace(url, f" URL_TOKEN_{i} ")
    # Remove mentions
    text = re.sub(r'@\S+', '', text)
    # Remove punctuation (keep URL placeholders)
    text = "".join(ch for ch in text if ch not in string.punctuation or ch in '._')
    # Tokenize
    words = nltk.word_tokenize(text)
    # Remove stopwords but keep URL placeholders
    words = [w for w in words if w not in stop_words or w.startswith('URL_TOKEN_')]
    return " ".join(words)

# ---------- 3. Text prediction function (your existing) ----------
def predict_text(message: str) -> str:
    """Return 'spam' or 'ham' for a given message."""
    cleaned = cleaning_data(message)
    transformed = text_vectorizer.transform([cleaned])
    prediction = text_model.predict(transformed)[0]
    return prediction

# ---------- 4. URL prediction function (your existing) ----------
def predict_url(url: str) -> str:
    """Return 'phishing' or 'safe' for a URL."""
    features = extract_url_features(url)
    X = url_vectorizer.transform([features])
    pred = url_model.predict(X)[0]
    return "phishing" if pred == 1 else "safe"

# ---------- 5. NEW: Combined classifier ----------
def is_fake_message(message: str) -> dict:
    """
    Determine if a message is 'fake' (phishing) or 'real' (safe).
    Returns dict with 'verdict' and 'reason'.
    """
    # Step 1: extract URLs from message
    urls = re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+|www\.[^\s<>"{}|\\^`\[\]]+', message, re.IGNORECASE)
    
    # Step 2: if any URL is phishing → message is fake
    for url in urls:
        if predict_url(url) == "phishing":
            return {"verdict": "fake", "reason": f"suspicious URL: {url}"}
    
    # Step 3: no suspicious URL → use text classifier
    text_result = predict_text(message)   # "spam" or "ham"
    
    if text_result == "spam":
        return {"verdict": "fake", "reason": "message text is suspicious"}
    else:
        return {"verdict": "real", "reason": "no suspicious content"}

# ---------- 6. Example usage (when script run directly) ----------
if __name__ == "__main__":
    test_messages = [
        "Click here to verify your account: http://hshhdy.vuuu",
        "Your invoice is attached: https://bit.ly/3xyz123",
        "Hey, let's meet for coffee tomorrow.",
        "CONGRATULATIONS! You've won $1000. Claim now: http://fake-reward.xyz"
    ]
    
    for msg in test_messages:
        result = is_fake_message(msg)
        print(f"\nMessage: {msg[:60]}...")
        print(f"Verdict: {result['verdict']} | Reason: {result['reason']}")