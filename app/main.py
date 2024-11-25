# app/main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
from app.config import settings
from app.database import Base, engine
from app.routes import users
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para sistema de gestión de ejercicios",
    version="0.1.0"
)

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Manejador global de excepciones
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={"message": "Database error occurred"}
    )

app.include_router(users.router, prefix=settings.API_V1_STR)

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
