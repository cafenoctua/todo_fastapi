from sqlalchemy.orm import Session
from sqlalchemy import sql
from .. import models, schemas

def get_todoitem(db: Session, todoitem_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todoitem_id).first()

def all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_user_todo(db: Session, user_name: str):
    return db.query(models.Todo).filter(models.Todo.user_name==user_name).all()

def create(db: Session, todo: schemas.Todo):
    db_todoitem = models.Todo(title=todo.title, description=todo.description, status=todo.status, user_name=todo.user_name)
    db.add(db_todoitem)
    db.commit()
    db.refresh(db_todoitem)
    return db_todoitem

def edit_todoitem(db: Session, todoitem_id: int, todo: schemas.Todo):
    item = db.query(models.Todo).filter(models.Todo.id == todoitem_id).first()
    item.title = todo.title
    item.description = todo.description
    db.commit()
    return item

def delete_todoitem(db: Session, todoitem_id: int):
    item = db.query(models.Todo).filter(models.Todo.id == todoitem_id).first()
    db.delete(item)
    db.commit()
    return item