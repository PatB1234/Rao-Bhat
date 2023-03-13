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

@app.get("/get_add_member")
def get_add_member(request: Request):

    return templates.TemplateResponse("addMember.html", {"request": request})

@app.get("/get_edit_member")
def get_add_member(request: Request):

    return templates.TemplateResponse("editMember.html", {"request": request})


@app.get("/get_tree")
def get_tree():
     
    return db.get_tree()

@app.post("/add_member")
def add_member(name: str = Form(...), mid: int = Form(...), fid: int = Form(...), pid: int = Form(...), married: bool = Form(False), gender: str = Form(...), place: str = Form(...)):

        tMid = mid
        tFid = fid
        tPid = pid

        if (married != True):

            if (mid < 0):
                    
                    tMid = None
                    tFid = None
                    tPid = None
                
            else: 

                tPid = None


        else:
                
                if (mid < 0):

                    #, "Born": data[1], "Place": data[3], "Marraige": data[4]
                    tMid = None
                    tFid = None
                else: 

                    #, "Born": data[1], "Place": data[3], "Marraige": data[4] 
                    pass

        return db.add_human(name, tMid, tFid, tPid, gender, married, place)

@app.post("/edit_node")
def edit_node(ids: int = Form(...), name: str = Form(...), mid: int = Form(...), fid: int = Form(...), pid: int = Form(...), married: bool = Form(False), gender: str = Form(...), place: str = Form(...)):
     
        tMid = mid
        tFid = fid
        tPid = pid

        if (married != True):

            if (mid < 0):
                    
                    tMid = None
                    tFid = None
                    tPid = None
                
            else: 

                tPid = None


        else:
                
                if (mid < 0):

                    #, "Born": data[1], "Place": data[3], "Marraige": data[4]
                    tMid = None
                    tFid = None
                else: 

                    #, "Born": data[1], "Place": data[3], "Marraige": data[4] 
                    pass

        return db.edit_node(ids, gender, name, tPid, tMid, tFid, place, married)
