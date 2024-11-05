from sqlalchemy import Column, Integer

from src.db.session import Base


class BaseModel(Base):
    """Base model"""
    id = Column(Integer, primary_key=True, index=True, unique=True)