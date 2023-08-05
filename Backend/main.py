from fastapi import FastAPI, Form, status, Depends
from fastapi.security.oauth2 import OAuth2
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db import *

app = FastAPI()
app.mount("/", StaticFiles(directory="/"), name="/")


@app.post("/create_tables")
def post_create_tables():

    return create_tables()


@app.post("/create_user")
def post_create_user(name: str, age: int, birthday: str, deathDate: str, pids: str, mid: int, fid: int):
    print(name, age, birthday, deathDate, pids, mid, fid)
    create_user(name, age, birthday, deathDate, pids, mid, fid)


@app.get("/users")
def get_users():

    return get_all_users()


@app.post("/update_name")
def post_update_name(name, uid):

    return update_name(name, uid)


@app.post("/update_age")
def post_update_name(age, uid):

    return update_age(age, uid)
