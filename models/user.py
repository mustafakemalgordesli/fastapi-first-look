from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int 
    firstName: str
    lastName: str
    password: str
    email: EmailStr
    status: bool = True
