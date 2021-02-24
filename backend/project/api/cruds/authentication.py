from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import sql
from passlib.context import CryptContext
from ..utils import token

from .. import models, schemas

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password: str, plain_password: str):
        return pwd_cxt.verify(plain_password, hashed_password)


def register(db: Session, data: schemas.Users):
    email = db.query(models.Users).filter(models.Users.email == data.email)
    user_name = db.query(models.Users).filter(models.Users.name == data.name)
    if email.first() or user_name.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Exsits email or name. Please input other's.")
    
    user = models.Users(name=data.name, email=data.email,
                        password=Hash.bcrypt(data.password))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db: Session, request: OAuth2PasswordRequestForm):
    user = db.query(models.Users).filter(models.Users.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials. Please input correct user name or email.")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}