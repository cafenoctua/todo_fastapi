from typing import Optional, List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..cruds import authentication
from .. import schemas
from ..utils import auth_func

router = APIRouter(
    prefix="/authentication",
    tags=["authentication"]
)

@router.post("/register", response_model=schemas.ShowUser)
def register(data: schemas.Users, db: Session = Depends(get_db)):
    return authentication.register(db, data)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authentication.login(db, request)

@router.post("/{user_id}/logout")
def logout(user_id: str, db: Session = Depends(get_db), current_user: schemas.Users = Depends(auth_func.get_current_user)):
    return authentication.logout(user_id, db)