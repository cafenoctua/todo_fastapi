from typing import List

from fastapi import FastAPI
from sqlalchemy.orm import Session

from . import models
from .routers import todo, user
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo.router)
app.include_router(user.router)
