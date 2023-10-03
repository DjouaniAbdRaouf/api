from fastapi import APIRouter
from config.db import db
from models.user import users
from schemas.user import Users

user_route = APIRouter()


@user_route.get("/")
async def get_users():
    return db.execute(users.select()).fetchall()


@user_route.get("/{id}")
async def get_data_user(id: str):
    return db.execute(users.select().where(id == users.c.id)).fetchall()


@user_route.post("/")
async def write_data(user_add: Users):
    db.execute(users.insert().values(
        name=user_add.name,
        email=user_add.email,
        pasaword=user_add.password
    ))
    return {"users": db.execute(users.select()).fetchall(), "msg": "user added"}


@user_route.get("/{id}")
async def update_user(id: int, user_update: Users):
    result = db.execute(users.update(
        name=user_update.name,
        email=user_update.email,
        password=user_update.password
    ).where(
        id == users.c.id
    ))
    if result:
        return {"users": db.execute(users.select()).fetchall(), "msg": "users added"}
    else:
        return {"msg": "failed to update"}


@user_route.delete("/{id}")
async def delete_data(id:int):
    db.execute(users.delete().where(users.c.id == id))
    return {"users": db.execute(users.select()).fetchall(), "msg": "user deleted"}