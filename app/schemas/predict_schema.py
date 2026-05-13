from pydantic import BaseModel


class PredictionRequest(BaseModel):
    message: str