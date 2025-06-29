# day_2_fast_api/crud/todo.py
from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException

from day_2_fast_api.models.todo import ToDo, ToDoCreate, ToDoUpdate

async def create_todo_item(db: Session, todo_create: ToDoCreate) -> ToDo:
    db_todo = ToDo.model_validate(todo_create) # Convert Pydantic model to SQLModel instance
    db.add(db_todo)
    await db.commit() # Asynchronous commit
    await db.refresh(db_todo) # Refresh to get auto-generated ID
    return db_todo

async def get_todo_items(db: Session, skip: int = 0, limit: int = 100) -> List[ToDo]:
    statement = select(ToDo).offset(skip).limit(limit)
    result = await db.exec(statement) # Asynchronous execution
    todos = result.all()
    return todos

async def get_todo_item(db: Session, todo_id: int) -> Optional[ToDo]:
    return await db.get(ToDo, todo_id) # Asynchronous get by primary key

async def update_todo_item(db: Session, todo_id: int, todo_update: ToDoUpdate) -> ToDo:
    db_todo = await db.get(ToDo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")

    # Use .sqlmodel_update() method from SQLModel to update fields
    todo_data = todo_update.model_dump(exclude_unset=True) # Only update fields that are set
    for key, value in todo_data.items():
        setattr(db_todo, key, value)

    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo

async def delete_todo_item(db: Session, todo_id: int):
    db_todo = await db.get(ToDo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    await db.delete(db_todo)
    await db.commit()
    return {"message": "To-Do item deleted successfully"}