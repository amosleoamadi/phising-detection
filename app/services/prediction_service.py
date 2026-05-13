# app/services/prediction_service.py

from app.predict import predict_text
from app.predict_url import predict_url
from app.utils.helpers import is_url


def predict_input(text: str):

    # URL PATH
    if is_url(text):
        result = predict_url(text)

        return {
            "type": "url",
            "result": result,
            "prediction": "The URL is likely phishing." if result == "phishing" else "The URL is safe."
        }

    # TEXT PATH
    result = predict_text(text)

    return {
        "type": "text",
        "result": result,
        "prediction": "The message is likely phishing." if result == "spam" else "The message is safe."
    }