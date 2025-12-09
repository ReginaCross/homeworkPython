import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def db_engine():
    """Создание подключения к БД"""
    
    DB_USER = os.getenv("DB_USER", "myuser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "mydatabase")
    
    
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    engine = create_engine(DATABASE_URL)
    
    
    Base.metadata.create_all(engine)
    
    yield engine
    
    
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Создание сессии для каждого теста"""
    Session = sessionmaker(bind=db_engine)
    session = Session()
    
    yield session
    
    
    session.rollback()
    session.close()