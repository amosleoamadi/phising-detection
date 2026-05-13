import joblib

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")



def predict_text(message: str):

    transformed = vectorizer.transform([message])

    prediction = model.predict(transformed)

    return prediction[0]