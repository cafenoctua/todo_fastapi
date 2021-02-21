from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..cruds import user
from ..database import get_db
from .. import schemas

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/")
def create_user(data: schemas.Users, db: Session = Depends(get_db)):
    return user.create(db, data)
