# todo_app/models/todo.py
from typing import Optional
from sqlmodel import Field, SQLModel

# Using SQLModel which combines Pydantic for validation and SQLAlchemy for ORM
class ToDoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)

class ToDo(ToDoBase, table=True): # table=True makes it a SQLAlchemy model
    id: Optional[int] = Field(default=None, primary_key=True)

class ToDoCreate(ToDoBase): # Model for creating (ID is auto-generated)
    pass

class ToDoUpdate(SQLModel): # Model for updating (all fields are optional)
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None