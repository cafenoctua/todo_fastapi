from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..cruds import todo
from .. import schemas

router = APIRouter(
    prefix="/todo",
    tags=["todo"]
)


@router.post("/", response_model=schemas.Todo)
def post_todo(data: schemas.Todo, db: Session = Depends(get_db)):
    return todo.create(db, data)


@router.get("/", response_model=List[schemas.ShowTodo])
def get_all_todo(db: Session = Depends(get_db), skip: Optional[int] = 0, limit: Optional[int] = 100):
    return todo.all(db, skip, limit)


@router.get("/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return todo.get_todo(db, todo_id)


@router.get("/users/{user_name}", response_model=List[schemas.TodoUser])
def get_user_todo(user_name: str, db: Session = Depends(get_db)):
    return todo.get_user_todo(db, user_name)


@router.put("/{todo_id}")
def update(todo_id: int, request: schemas.Todo, db: Session = Depends(get_db)):
    return todo.update_todo(db, todo_id, request)


@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    return todo.delete_todo(db, todo_id)
