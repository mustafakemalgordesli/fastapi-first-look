import os
import sys 
sys.path.append(os.getcwd())
from models.user import User
from sqlalchemy.orm import sessionmaker
from config.db import Session, User

class UserController:
    def create(user):
        session = Session()
        createdUser = User()
        createdUser.id = 0
        createdUser.email = user.email
        createdUser.password = user.password
        createdUser.firstName = user.firstName
        createdUser.lastName = user.lastName
        createdUser.status = user.status
        session.add(createdUser)
        session.commit()
        session.close()
        return user

        