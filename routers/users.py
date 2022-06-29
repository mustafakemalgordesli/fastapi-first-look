import sys 
from fastapi import APIRouter
import os

sys.path.append(os.getcwd())
from models.user import User
from controllers.users import UserController


router = APIRouter()


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]



@router.get("/{id}", tags=["users"])
async def read_user(id: int):
    return {"username": id}


@router.post("/", response_model=User)
async def create_user(user: User):
    return UserController.create(user)
