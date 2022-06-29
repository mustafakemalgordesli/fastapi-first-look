from pydantic import BaseModel, EmailStr
from datetime import datetime
from fastapi import Body
class User(BaseModel):
    id: int 
    firstName: str
    lastName: str
    password: str
    email: EmailStr
    createdAt: datetime = datetime.now()
    updatedAt: datetime or  None = Body(default=None)
    status: bool = True
