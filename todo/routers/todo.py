from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter()

@router.get("/todo", response_model=List[schemas.Todo])
def get_todos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos

@router.post("/todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(database.get_db)):
    return crud.create_todo(db, todo=todo)

@router.put("/todo/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(database.get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.delete("/todo/{todo_id}", response_model=schemas.Todo)
def delete_todo(todo_id: int, db: Session = Depends(database.get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo
