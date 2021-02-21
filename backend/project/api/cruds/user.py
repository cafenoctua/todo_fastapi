from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import sql
from .. import models, schemas


def create(db: Session, data: schemas.Users):
    email = db.query(models.Users).filter(models.Users.email == data.email)
    user_name = db.query(models.Users).filter(models.Users.name == data.name)
    if email.first() or user_name.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Exsits email or name. Please input other's.")

    user = models.Users(name=data.name, email=data.email,
                        password=data.password)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
