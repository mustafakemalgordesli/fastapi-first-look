import os
import sys 
sys.path.append(os.getcwd())
from models.user import User
from sqlalchemy.orm import sessionmaker
from config.db import Session, User

class UserController:
    def create(user):
        try:
            session = Session()
            createdUser = User()
            createdUser.id = 0
            createdUser.email = user.email
            createdUser.password = user.password
            createdUser.firstName = user.firstName
            createdUser.lastName = user.lastName
            createdUser.status = user.status
            createdUser.createdAt = user.createdAt
            session.add(createdUser)
            session.commit()
            session.close()
            return user
        except Exception as e:
            print(e)
            return { "message": "user failed to register", "success": False}

        