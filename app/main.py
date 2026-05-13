from fastapi import FastAPI
from app.routes.predictor import router 

app = FastAPI(title="Phishing Detection API")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "API Running"}