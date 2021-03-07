from typing import Optional, List
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str

class Users(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True

class UserPass(BaseModel):
    password: str

class ShowUsers(BaseModel):
    id: List[str]

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str

    class Config():
        orm_mode = True

class Todo(BaseModel):
    title: str
    description: str
    status: str
    user_name: str

    class Config():
        orm_mode = True


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

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
