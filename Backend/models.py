from pydantic import BaseModel


class User(BaseModel):

    id: int
    name: str
    age: int
    Birthday: str
    DeathDate: str = 0
    Spouse: list[int] = 0
    Mother: int = 0
    Father: int = 0


class User2(BaseModel):

    id: int
    name: str
    age: int
    Birthday: str
    DeathDate: str = ""
    Spouse: str = ""
    Mother: str = ""
    Father: str = ""


class User3(BaseModel):

    uid: int
    newId: int


class User4(BaseModel):

    uid: int
    name: str
    age: int
    Birthday: str
    DeathDate: str = 0
