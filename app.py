from ast import Num
from fastapi import FastAPI
from routers import users


app = FastAPI(debug=True)


@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}

app.include_router(users.router, prefix="/users", tags=["users"])
