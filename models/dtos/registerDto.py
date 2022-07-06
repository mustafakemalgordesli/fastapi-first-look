from pydantic import BaseModel, EmailStr
from datetime import datetime

class RegisterDto(BaseModel): 
    firstName: str
    lastName: str
    password: str
    email: EmailStr
