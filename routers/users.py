import sys 
from fastapi import APIRouter
import os

sys.path.append(os.getcwd())
from models.dtos.loginDto import LoginDto
from models.dtos.registerDto import RegisterDto
from controllers.users import UserController


router = APIRouter()




@router.post("/register")
async def register(user: RegisterDto):
    return UserController.create(user)


@router.post("/login")
async def login(user: LoginDto):
    return "login"
