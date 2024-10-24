from datetime import timedelta
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.config import settings
from src.app.base.utils.db import get_db

from src.app.user import models
from src.app.user import schemas
from src.app.user import crud

from .schemas import Token, Msg, VerificationInDB
from .logic import get_current_user
from .jwt import create_access_token
from .security import get_password_hash
from .send_email import send_reset_password_email
from .logic import (
    generate_password_reset_token,
    verify_password_reset_token,
    registration_user,
    verify_registration_user
)


auth_router = APIRouter()

@auth_router.post("/login/access-token", response_model=Token)
def login_access_token(
        db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud.user.authenticate(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user.id}, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }

@auth_router.post("/registration", response_model=Msg)
def user_registration(new_user: schemas.UserCreateInRegistration, db: Session = Depends(get_db)):
    """Resgister a new user"""
    user = registration_user(new_user, db)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        return {"msg": "Send email"}

@auth_router.post("/confirm-email", response_model=Msg)
def confirm_email(uuid: VerificationInDB, db: Session = Depends(get_db)):
    if verify_registration_user(uuid, db):
        return {"msg": "Success verify email"}
    else:
        raise HTTPException(status_code=404, detail="Not found")

@auth_router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(get_current_user)):
    """Test access token"""
    return current_user

@auth_router.post("/password-recovery/{email}", response_model=Msg)
def recover_password(email: str, db: Session = Depends(get_db)):
    """Recover password"""
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with username does not exist in the system. ",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}

@auth_router.post("/reset-password/", response_model=Msg)
def reset_password(token: str = Body(...), new_password: str = Body(...), db: Session = Depends(get_db)):
    """Reset password"""
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}












