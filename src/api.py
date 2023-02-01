from src import db
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import status, Form
from fastapi.param_functions import Depends
from pydantic import BaseModel
from pydantic.errors import FrozenSetError
from starlette.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
import jinja2

app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/render_temp")
def render_temp(request: Request):

    return templates.TemplateResponse("FamilyTree.html", {"request": request})

@app.get("/get_tree")
def get_tree():

    return db.get_tree()
