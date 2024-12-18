import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from src.config import settings

from src.app.user import schemas
from src.app.user import crud
from .crud import auth_verify
from .send_email import send_new_account_email
from .schemas import VerificationOut, VerificationCreate

password_reset_jwt_subject = "preset"


def registration_user(new_user: schemas.UserCreateInRegistration, db: Session) -> bool:
    """Register a new user"""
    if crud.user.get_by_username_email(db, username=new_user.username, email=new_user.email):
        return True
    else:
        user = crud.user.create(db, schema=new_user)
        verify = auth_verify.create(db, schema=VerificationCreate(user_id=user.id))
        send_new_account_email(new_user.email, new_user.username, new_user.password, verify.link)
        return False


def verify_registration_user(uuid: VerificationOut, db: Session) -> bool:
    """confirmation of the user's email"""
    verify = auth_verify.get(db, link=uuid.link)
    if verify:
        user = crud.user.get(db, id=verify.user_id)
        crud.user.update(db, model=user, schema=schemas.UserUpdate(**{"is_active": "True"}))
        auth_verify.remove(db, uuid.link)
        return True
    else:
        return False


def generate_password_reset_token(email: str):
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": password_reset_jwt_subject, "email": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        assert decoded_token["sub"] == password_reset_jwt_subject
        return decoded_token["email"]
    except InvalidTokenError:
        return None
