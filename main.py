from fastapi import FastAPI
from typing import Union
from app.routers import user_router

app = FastAPI()

@app.get("/health")
def read_root():
    return {"status": 'ok'}

app.include_router(user_router.router)

@app.get("/user/{userId}")
def get_user(userId: int):
    return {"userId": userId, "mensagem": f"Retornando o usuario {userId}"}