from sqlalchemy import Column, String, DateTime, Boolean, sql

from src.app.base.model_base import BaseModel


class User(BaseModel):
    __tablename__ = 'user_user'

    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String(150))
    last_name = Column(String(150))
    date_join = Column(DateTime(timezone=True), server_default=sql.func.now())
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=True)
    avatar = Column(String)
