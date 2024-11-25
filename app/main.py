# app/main.py
from fastapi import FastAPI
from typing import Dict
from app.config import settings
from app.routes import users

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para sistema de gestión de ejercicios",
    version="0.1.0"
)

app.include_router(users.router)


@app.get("/", response_model=Dict[str, str])
def read_root() -> Dict[str, str]:
    return {"message": "¡Bienvenido a FitTrack API!"}

@app.get("/health", response_model=Dict[str, str])
def health_check() -> Dict[str, str]:
    return {"status": "operativo"}

@app.get("/exercises/example", response_model=Dict[str, str | int])
def exercise_example() -> Dict[str, str | int]:
    return {
        "name": "Flexiones",
        "type": "Peso corporal",
        "repetitions": 10
    }