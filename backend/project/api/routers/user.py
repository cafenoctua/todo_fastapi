from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..cruds import user
from ..database import get_db
from .. import schemas
from ..utils import auth_func

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/{user_id}", response_model=schemas.User)
def get(user_id: str, db: Session = Depends(get_db), current_user: schemas.Users = Depends(auth_func.get_current_user)):
    return user.get(user_id, db)


@router.get("/", response_model=schemas.ShowUsers)
def get_active_user(db: Session = Depends(get_db), current_user: schemas.Users = Depends(auth_func.get_current_user)):
    return user.get_active(db)

@router.put("/{user_id}/edit")
def edit(user_id: str, user_data: schemas.Users, db: Session = Depends(get_db), current_user: schemas.Users = Depends(auth_func.get_current_user)):
    return user.edit(user_id, user_data, db)

@router.delete("/{user_id}/delete")
def delete(user_id: str, user_data: schemas.UserPass, db: Session = Depends(get_db), current_user: schemas.Users = Depends(auth_func.get_current_user)):
    return user.delete(user_id, user_data.password, db)

