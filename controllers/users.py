from database.db import Session, User
from cgitb import reset
import datetime
import os
import sys
sys.path.append(os.getcwd())


class UserController:
    def create(data):
        try:
            session = Session()
            createdUser = User(email=data.email, firstName=data.firstName,
                                lastName=data.lastName, password=data.password)
            session.add(createdUser)
            session.commit()
            session.refresh(createdUser)
            session.close()
            return {"data": createdUser, "data2": data}
        except Exception as e:
            print("Hata:")
            print(e)
            return {"message": "user failed to register", "success": False}

    def login(data):
        return {"message": "user failed to login", "success": False}
