import joblib

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

print(type(vectorizer))
print(vectorizer)



def predict_text(message: str):

    transformed = vectorizer.transform([message])

    prediction = model.predict(transformed)

    return prediction[0]