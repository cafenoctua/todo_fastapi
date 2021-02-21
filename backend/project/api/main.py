from typing import List

from fastapi import FastAPI
from sqlalchemy.orm import Session

from . import models
from .routers import todo
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo.router)
