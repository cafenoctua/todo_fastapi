from datetime import timedelta
from datetime import datetime

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import sql

from ..utils import auth_func
from .. import models, schemas


def register(db: Session, data: schemas.Users):
    email = db.query(models.Users).filter(models.Users.email == data.email)
    user_name = db.query(models.Users).filter(models.Users.name == data.name)
    if email.first() or user_name.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Exsits email or name. Please input other's.")

    user = models.Users(name=data.name, email=data.email,
                        password=auth_func.Hash.bcrypt(data.password))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


ACCESS_TOKEN_EXPIRE_MINUTES = 30
def login(db: Session, request: OAuth2PasswordRequestForm):
    if "@" in request.username:
        user_update = db.query(models.Users).filter(
            models.Users.email == request.username)
        user = user_update.first()
    else:
        user_update = db.query(models.Users).filter(
            models.Users.name == request.username)
        user = user_update.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials. Please input correct user name or email.")

    if not auth_func.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_func.create_access_token(data={"sub": user.name}, expires_delta=access_token_expires)
    user_update.update({"logined": True})
    db.commit()

    return {"access_token": access_token, "token_type": "bearer"}

def logout(user_id: str, db: Session):
    user = db.query(models.Users).filter(models.Users.id == user_id)
    user.update({"logined": False})
    db.commit()
    return "Done"