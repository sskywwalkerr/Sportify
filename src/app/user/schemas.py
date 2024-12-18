from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str] = None


class UserBaseInDB(UserBase):
    id: int = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

    class Config:
        from_attributes = True


class UserCreate(UserBaseInDB):
    """ Свойства для получения через API при создании из админки
    """
    username: str
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None


class UserCreateInRegistration(BaseModel):
    """ Свойства для получения через API при регистрации
    """
    username: str
    email: EmailStr
    password: str
    first_name: str

    class Config:
        from_attributes = True


class UserUpdate(UserBaseInDB):
    """ Properties to receive via API on update
    """
    password: Optional[str] = None


class User(UserBaseInDB):
    """ Additional properties to return via API
    """
    pass


class UserInDB(UserBaseInDB):
    """ Additional properties stored in DB
    """
    password: str


class SocialAccount(BaseModel):
    """Schema social account"""
    account_id: int
    account_url: str
    account_login: str
    account_name: str
    avatar_url: str
    provider: str

    class Config:
        from_attributes = True


class UserPublic(UserBase):
    """ For public profile user
    """
    id: int
    # social_account: SocialAccount

    class Config:
        from_attributes = True
