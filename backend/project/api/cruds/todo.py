from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import sql
from .. import models, schemas


def all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def get_todo(db: Session, todo_id: int):
    item = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sorry, not found id: {todo_id} todo item.")

    return item.first()


def get_user_todo(db: Session, user_name: str):
    items = db.query(models.Todo).filter(models.Todo.user_name == user_name)
    if not items.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sorry, not found {user_name}'s todo item.")
    return items.all()


def create(db: Session, todo: schemas.Todo):
    db_todoitem = models.Todo(title=todo.title, description=todo.description,
                              status=todo.status, user_name=todo.user_name)
    if type(todo.title) != str or type(todo.description) != str or type(todo.status) != str or type(todo.user_name) != str:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="All parameter type is string. Please input string type.")
    db.add(db_todoitem)
    db.commit()
    db.refresh(db_todoitem)
    return db_todoitem


def update_todo(db: Session, todo_id: int, request: schemas.Todo):
    item = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sorry, not found id: {todo_id} todo item.")
    item.update(request)
    db.commit()
    return "Updated"


def delete_todo(db: Session, todo_id: int):
    item = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sorry, not found id: {id} todo item.")
    item.delete(synchronize_session=False)
    db.commit()
    return "Done"
