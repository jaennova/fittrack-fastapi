# app/__init__.py
from app.database import Base, engine

def init_db():
    Base.metadata.create_all(bind=engine)