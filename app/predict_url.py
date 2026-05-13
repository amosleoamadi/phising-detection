import joblib
from app.utils.url_features import extract_url_features


# Load the trained model and vectorizer
model = joblib.load("models/url_model.pkl")
vectorizer = joblib.load("models/url_vectorizer.pkl")
print(type(vectorizer))
print(vectorizer)

def predict_url(url: str):

    # Extract feature dictionary
    features = extract_url_features(url)
    print(features)
    print(type(features))

    # Convert dictionary into ML format
    transformed_features = vectorizer.transform([features])

    # Predict
    prediction = model.predict(transformed_features)

    result = prediction[0]

    if result == 1:
        return "phishing"

    return "safe"
