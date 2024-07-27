from pydantic import BaseModel
from typing import Optional, List


class TodoBase(BaseModel):
  title: str
  description: Optional[str] = None


class TodoCreate(TodoBase):
  pass 

class TodoUpdate(TodoBase):
  pass

class TodoInDB(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class Todo(TodoInDB):
    pass

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserResponse(UserBase):
    id: int
    is_active: bool
    todos: List[TodoInDB] = []
