from fastapi import FastAPI
from fastapi import status, Form
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from db import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():

    return RedirectResponse("/static/index.html", status.HTTP_302_FOUND)


@app.post("/create_tables")
def post_create_tables():

    create_tables()


@app.post("/create_user")
def post_create_user(name: str = Form(...), age: int = Form(...), birthday: str = Form(...), deathDate: str = Form(...), pids: str = Form(...), mid: int = Form(...), fid: int = Form(...)):

    create_user(name, age, birthday, deathDate, pids, mid, fid)


@app.get("/get_users")
def get_users():

    return get_all_users()


@app.post("/update_name")
def post_update_name(name: int = Form(...), uid: int = Form(...)):

    update_name(name, uid)


@app.post("/update_age")
def post_update_age(age: int = Form(...), uid: int = Form(...)):

    update_age(age, uid)


@app.post("/update_birthday")
def post_update_birthday(birthday: str = Form(...), uid: int = Form(...)):

    update_birthday(birthday, uid)


@app.post("/update_deathdate")
def post_update_deathdate(deathDate: str = Form(...), uid: int = Form(...)):

    update_deathDate(deathDate, uid)


@app.post("/update_pids")
def post_update_pids(pids: str = Form(...), uid: int = Form(...)):

    update_pids(pids, uid)


@app.post("/update_mid")
def post_update_mid(mid: int = Form(...), uid: int = Form(...)):

    update_mid(mid, uid)


@app.post("/update_fid")
def post_update_fid(fid: int = Form(...), uid: int = Form(...)):

    update_fid(fid, uid)


@app.post("/remove_user")
def post_remove_user(uid: int = Form(...)):

    remove_user(uid)
