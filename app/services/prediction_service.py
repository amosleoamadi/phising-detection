from app.predict import predict_text
from app.predict_url import predict_url

from app.utils.helpers import is_url


def predict_message(message: str):

    # URL detection
    if is_url(message):

        result = predict_url(message)

        if result == "phishing":
            return "phishing"

        return "safe"

    # Text detection
    result = predict_text(message)

    if result == "spam":
        return "phishing"

    return "safe"