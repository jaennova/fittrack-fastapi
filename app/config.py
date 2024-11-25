# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./fittrack.db"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FitTrack API"

    class Config:
        case_sensitive = True

settings = Settings()