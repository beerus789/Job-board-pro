# todo_app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from day_2_fast_api.database import create_db_and_tables, get_session
from day_2_fast_api.models.todo import ToDo, ToDoCreate, ToDoUpdate
from day_2_fast_api.crud import todo as crud_todo

app = FastAPI(
    title="Production-Ready To-Do API",
    description="A To-Do API demonstrating async, PostgreSQL/SQLModel, and modular design.",
    version="1.0.0"
)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Production-Ready To-Do API! Visit /docs for API documentation."}

@app.post("/todos/", response_model=ToDo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: ToDoCreate, db: Session = Depends(get_session)):
    """
    Create a new To-Do item.
    """
    return await crud_todo.create_todo_item(db, todo)

@app.get("/todos/", response_model=List[ToDo])
async def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    """
    Retrieve a list of all To-Do items.
    """
    return await crud_todo.get_todo_items(db, skip=skip, limit=limit)

@app.get("/todos/{todo_id}", response_model=ToDo)
async def read_todo_by_id(todo_id: int, db: Session = Depends(get_session)):
    """
    Retrieve a single To-Do item by its ID.
    """
    db_todo = await crud_todo.get_todo_item(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return db_todo

@app.put("/todos/{todo_id}", response_model=ToDo)
async def update_todo(todo_id: int, todo: ToDoUpdate, db: Session = Depends(get_session)):
    """
    Update an existing To-Do item.
    """
    return await crud_todo.update_todo_item(db, todo_id, todo)

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: Session = Depends(get_session)):
    """
    Delete a To-Do item by its ID.
    """
    await crud_todo.delete_todo_item(db, todo_id)
    return