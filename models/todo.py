from pydantic import BaseModel
from fastapi import Body
from datetime import datetime

class User(BaseModel):
    id: int 
    todo: str
    userId: int
    deadline: datetime or  None = Body(default=None),
    createdAt: datetime = datetime.now()
    updatedAt: datetime or  None = Body(default=None)
    isCompleted: bool = False
    isDeleted: bool = False