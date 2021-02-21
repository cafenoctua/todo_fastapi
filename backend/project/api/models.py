from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    # group_id = relationship("Groups", back_populates="user")
    todo_id = relationship("Todo", back_populates="user")

# class Groups(Base):
#     __tablename__ = "groups"

#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
#     name = Column(String)
#     user_name = Column(Integer, ForeignKey('users.name'))

#     user = relationship("Users", back_populates="group_id")
#     todo_id = relationship("Todo", back_populates="group")

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    user_name = Column(String, ForeignKey('users.name'))
    # group_name = Column(String, ForeignKey('groups.name'))

    user = relationship("Users", back_populates="todo_id")
    # group = relationship("Groups", back_populates="todo_id")
