from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    """Модель студента с поддержкой soft delete"""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)  
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

class Course(Base):
    """Модель курса/предмета"""
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    is_active = Column(Boolean, default=True, nullable=False)  
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}')>"