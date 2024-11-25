# app/models/__init__.py
from app.database import Base, engine
from app.models.user import User

def init_db() -> None:
    Base.metadata.create_all(bind=engine)