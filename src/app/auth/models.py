from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from src.db.session import Base


class Verification(Base):
    """models for verification registration users"""
    __tablename__ = 'auth_verification'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    link = Column(UUID(as_uuid=True), default=uuid4)
    user_id = Column(Integer, ForeignKey("user.id"))