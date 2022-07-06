from cgitb import reset
import datetime
import os
import sys 
sys.path.append(os.getcwd())
from config.db import Session, User

class UserController:
    def create(data):
        try:
            session = Session()
            # createdUser = User(email=data.email, firstName=data.firstName, lastName=data.lastName, password=data.password)
            #createdUser = User(id=2, email=data.email, firstName=data.firstName, lastName=data.lastName, password=data.password, createdAt=datetime.now(), status=True)
            createdUser = User()
            createdUser.email = data.email
            createdUser.firstName = data.firstName
            createdUser.lastName = data.lastName
            createdUser.status = True
            createdUser.password = data.password
            createdUser.createdAt = datetime.datetime.now()
            session.add(createdUser)
            session.commit()
            session.refresh(createdUser)
            session.close()
            return { "data": createdUser, "data2":data }
        except Exception as e:
            print("Hata:")
            print(e)
            return { "message": "user failed to register", "success": False}
    
    def login(data):
        return { "message": "user failed to login", "success": False}

        