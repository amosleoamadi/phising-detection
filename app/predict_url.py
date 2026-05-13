import joblib
from app.utils.url_features import extract_url_features


# Load the trained model and vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_url(url: str):

    # Extract features from URL
    features = extract_url_features(url)

    # Convert features into ML format
    transformed_features = vectorizer.transform([features])

    # Predict
    prediction = model.predict(transformed_features)

    results = prediction[0]
    if results == 1:
        return "phishing"

    return "safe"
