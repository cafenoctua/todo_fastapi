from typing import Optional, List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..cruds import authentication
from .. import schemas

router = APIRouter(
    prefix="/authentication",
    tags=["authentication"]
)

@router.post("/register", response_model=schemas.ShowUsers)
def register(data: schemas.Users, db: Session = Depends(get_db)):
    return authentication.register(db, data)

@router.post("/login", response_model=schemas.ShowUsers)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authentication.login(db, request)

# @router.post("/logout")
# def logout(request: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(get_db)):
#     return authentication.logout(db, request)