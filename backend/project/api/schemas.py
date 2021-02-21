from typing import Optional
from pydantic import BaseModel

class Users(BaseModel):
    name: str
    email: str
    password: str

class Todo(BaseModel):
    title:str
    description: str
    status: str
    user_name: str
    # class Config():
    #     orm_mode = True

class ShowTodo(BaseModel):
    title: str = None
    description: str = None
    status: str = None
    user_name: str = None
    class Config():
        orm_mode = True


class TodoUser(BaseModel):
    title: str = None
    description: str = None
    status: str = None
    user_name: str 
    class Config():
        orm_mode = True