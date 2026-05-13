from fastapi import APIRouter

from app.schemas.predict_schema import PredictionRequest
from app.services.prediction_service import predict_message

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post("/")
def predict(data: PredictionRequest):

    result = predict_message(data.message)

    if result == "phishing":
        output = "The input is likely a phishing attempt."
    else:
        output = "The input appears safe."

    return {
        "input": data.message,
        "result": result,
        "prediction": output
    }