from fastapi import FastAPI
from fastapi import status, Form
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles
from pydantic import Json
from starlette.responses import RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from models import *
from db import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():

    return RedirectResponse("/static/index.html", status.HTTP_302_FOUND)


@app.post("/create_tables")
def post_create_tables():

    create_tables()


@app.post("/create_user")
def post_create_user(name: str = Form(...), age: int = Form(...), Birthday: str = Form(...), DeathDate: str = Form(...), pids: str = Form(...), Mother: int = Form(...), Father: int = Form(...)):

    create_user(name, age, Birthday, DeathDate, pids, Mother, Father)


@app.get("/get_users")
def get_users():

    return get_all_users()


@app.post("/update_full")
def post_update_full(user: User2):

    update_full(user)


@app.post("/check_data")
def check_data_front(user: User2):

    res = check_data(user)
    if (len(res) == 1):

        update_full(convert_to_id(user))
        return JSONResponse(content=True)
    else:
        return res

# Update the values that are not updated when the Error checking software is run in the front end


@app.post("/update_rest")
def post_update_rest(user: User4):

    update_rest(user)


@app.post("/update_name")
def post_update_name(name: int = Form(...), uid: int = Form(...)):

    update_name(name, uid)


@app.post("/update_age")
def post_update_age(age: int = Form(...), uid: int = Form(...)):

    update_age(age, uid)


@app.post("/update_Birthday")
def post_update_Birthday(Birthday: str = Form(...), uid: int = Form(...)):

    update_Birthday(Birthday, uid)


@app.post("/update_DeathDate")
def post_update_DeathDate(DeathDate: str = Form(...), uid: int = Form(...)):

    update_DeathDate(DeathDate, uid)


@app.post("/update_spouse")
def post_update_spouse(user: User3):

    update_spouse(user)


@app.post("/update_Mother")
def post_update_Mother(user: User3):

    update_Mother(user)


@app.post("/update_Father")
def post_update_Father(user: User3):

    update_Father(user)


@app.post("/remove_user")
def post_remove_user(uid: int = Form(...)):

    remove_user(uid)


@app.post("/add_member")
def post_add_member():

    add_member()
