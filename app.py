import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

# Cargar el modelo entrenado
modelo_cargado = joblib.load("modelo_fraude.pkl")

# Crear la API
app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="""
REST API for real-time credit card fraud detection using a Random Forest model.

This API provides:
- Health check endpoint
- Prediction endpoint
- Automatic Swagger documentation

The application is containerized with Docker and deployed on AWS ECS Fargate.
""",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "API",
            "description": "General API endpoints."
        },
        {
            "name": "Fraud Detection",
            "description": "Fraud prediction endpoint."
        }
    ]
)

# Estructura de una transacción
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount_scaled: float


@app.get("/", tags=["API"])
def home():
    return {
        "api": "Credit Card Fraud Detection API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["API"])
def health():
    return {
        "status": "healthy",
        "model": "Random Forest",
        "version": "1.0.0"
    }


@app.post("/predict", tags=["Fraud Detection"])
def predict(transaction: Transaction):
    datos = pd.DataFrame([transaction.model_dump()])
    prediccion = modelo_cargado.predict(datos)
    probabilidad = modelo_cargado.predict_proba(datos)

    return {
        "prediction": "Fraud" if prediccion[0] == 1 else "Not Fraud",
        "class": int(prediccion[0]),
        "probabilities": {
            "not_fraud": f"{probabilidad[0][0] * 100:.2f}%",
            "fraud": f"{probabilidad[0][1] * 100:.2f}%"
        },
        "model": "Random Forest",
        "model_version": "1.0.0"
    }