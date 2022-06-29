import sys 
from fastapi import APIRouter
import os

sys.path.append(os.getcwd())
from models.user import User
from controllers.users import UserController


router = APIRouter()




@router.post("/register")
async def register(user: User):
    return UserController.create(user)

@router.post("/login")
async def login(user: User):
    return "login"
