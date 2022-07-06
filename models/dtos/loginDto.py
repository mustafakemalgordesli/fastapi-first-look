from pydantic import BaseModel, EmailStr
from datetime import datetime

class LoginDto(BaseModel): 
    password: str
    email: EmailStr
