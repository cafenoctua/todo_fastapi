from datetime import timedelta
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import sql
from .. import models, schemas
from ..utils import auth_func


def get(user_id: str, db: Session):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials. Please input correct id.")

    return {"id": user.id, "name": user.name, "email": user.email}

def get_active(db: Session):
    users = db.query(models.Users).all()
    users_id = []
    for user in users:
        if user.logined:
            users_id.append(user.id)
    return {"id": users_id}

def edit(user_id: int, user_data: schemas.Users, db: Session):
    user = db.query(models.Users).filter(models.Users.id == user_id)
    user.update({"name": user_data.name, "email": user_data.email, "password": auth_func.Hash.bcrypt(user_data.password)})
    db.commit()
    return user_data.name


def delete(user_id: int, password: str, db: Session):
    user = db.query(models.Users).filter(models.Users.id == user_id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found user id. Please input correct id.")

    if not auth_func.Hash.verify(user.first().password, password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")
    
    user.delete(synchronize_session=False)
    db.commit()
    return "Done"
