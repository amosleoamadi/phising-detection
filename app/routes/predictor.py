# app/routes/predictor.py

from fastapi import APIRouter
from app.schemas.predict_schema import PredictionRequest
from app.services.prediction_service import predict_input

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post("/")
def predict(data: PredictionRequest):

    result = predict_input(data.message)

    return {
        "input": data.message,
        **result
    }