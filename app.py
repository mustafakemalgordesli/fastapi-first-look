from ast import Num
from fastapi import FastAPI
from routers import users


app = FastAPI(debug=True)


@app.get("/")
async def read_user_me():
    return {"username": "fakecurrentuser"}

app.include_router(users.router, prefix="/users", tags=["users"])
