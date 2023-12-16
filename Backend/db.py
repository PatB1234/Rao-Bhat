from pydantic import BaseModel
import os
import sqlite3 as driver
from sqlite3.dbapi2 import Cursor

DATABASE_URL = 'db/users.db'


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


def create_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (uid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INT, Birthday TEXT, DeathDate TEXT, Spouse VARCHAR, Mother INT, Father INT);")


def create_user(name: str, age: int, Birthday: str, DeathDate: str, Spouse: str, Mother: int, Father: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"INSERT INTO users (name, age, Birthday, DeathDate, Spouse, Mother, Father) VALUES ('{name}', '{age}', '{Birthday}', '{DeathDate}', '{Spouse}', '{Mother}', '{Father}');")

    database.commit()


def get_all_users():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    database.commit()
    userForm = []

    for user in users:
        pid = user[5]
        if pid == "":

            pid = []
        elif "," not in pid:
            pid = [int(pid)]
        else:

            split = pid.split(",")
            pid = [int(x) for x in split]
        userForm.append(User(id=user[0], name=user[1], age=user[2], Birthday=user[3],
                        DeathDate=user[4], Spouse=pid, Mother=user[6], Father=user[7]))
    return userForm


def get_users_by_name(name):

    arr = []
    users = get_all_users()
    for i in users:
        if i.name == name:

            arr.append(i)

    return arr


def check_data(user: User):
    fields_with_conflict = {'uid': user.id}
    if (user.Father != ""):

        fathers = get_users_by_name(user.Father)
        if len(fathers) != 1:

            if 'Father' not in fields_with_conflict.keys():

                fields_with_conflict['Father'] = []
            fields_with_conflict['Father'].append(fathers)

    if (user.Mother != ""):

        Mothers = get_users_by_name(user.Mother)
        if len(Mothers) != 1:

            if 'Mother' not in fields_with_conflict.keys():

                fields_with_conflict['Mother'] = []
            fields_with_conflict['Mother'].append(Mothers)
        if len(Mothers) == 1:

            update_Mother(User3(uid=user.id, newId=Mothers[0].id))

    if (user.Spouse != ""):
        Spouses = get_users_by_name(user.Spouse)
        if len(Spouses) != 1:
            if 'Spouse' not in fields_with_conflict.keys():

                fields_with_conflict['Spouse'] = []
            fields_with_conflict['Spouse'].append(Spouses)

        if len(Spouses) == 1:

            update_spouse(User3(uid=user.id, newId=Spouses[0].id))

    return fields_with_conflict


def convert_to_id(user: User2):

    Spouse = ""
    Mother = ""
    Father = ""
    if (user.Spouse != ""):

        Spouse = int(get_users_by_name(user.Spouse)[0].id)

    if (user.Mother != ""):

        Mother = int(get_users_by_name(user.Mother)[0].id)
    if (user.Father != ""):

        Father = int(get_users_by_name(user.Father)[0].id)
    if (type(Spouse) != int):

        Spouse = 0
    if (type(Mother) != int):

        Mother = 0
    if (type(Father) != int):

        Father = 0

    newUser = User(id=user.id, name=user.name, age=user.age, Birthday=user.Birthday,
                   DeathDate=user.DeathDate, Spouse=[Spouse], Mother=Mother, Father=Father)
    return newUser


def update_full(user: User):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET name = '{user.name}', age = {int(user.age)}, Birthday = '{user.Birthday}', DeathDate = '{user.DeathDate}', Spouse = '{user.Spouse[0]}', Mother = {int(user.Mother)}, Father = {int(user.Father)} WHERE uid = {user.id};")
    database.commit()


def update_name(name: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"UPDATE users SET name = '{name}' WHERE uid = {uid};")
    database.commit()


def update_age(age: int, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"UPDATE users SET age = {age} WHERE uid = {uid};")
    database.commit()


def update_Birthday(Birthday: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET Birthday = '{Birthday}' WHERE uid = {uid};")
    database.commit()


def update_DeathDate(DeathDate: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET DeathDate = '{DeathDate}' WHERE uid = {uid};")
    database.commit()


def get_user_by_id(id: int):

    arr = []
    users = get_all_users()
    for i in users:
        if i.id == id:

            arr.append(i)

    return arr


def update_spouse(user: User3):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    userModel = get_user_by_id(user.uid)[0]
    oldSpouseData = get_user_by_id(userModel.Spouse[0])
    newSpouseData = get_user_by_id(user.newId)[0]
    if oldSpouseData != []:

        oldSpouseData = get_user_by_id(userModel.Spouse[0])[0]
        cursor.execute(
            f"UPDATE users SET Spouse = 0 WHERE uid = {oldSpouseData.id};")
    cursor.execute(
        f"UPDATE users SET Spouse = {user.uid} WHERE uid = {newSpouseData.id};")
    cursor.execute(
        f"UPDATE users SET Spouse = {user.newId} WHERE uid = {user.uid};")
    database.commit()


def update_Mother(user: User3):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET Mother = {user.newId} WHERE uid = '{user.uid}';")
    database.commit()


def update_Father(user: User3):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET Father = {user.newId} WHERE uid = '{user.uid}';")
    database.commit()


def remove_user(uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"DELETE FROM users WHERE uid = '{uid}'")
    database.commit()


def add_member():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"INSERT INTO users (name, age, Birthday, DeathDate, Spouse, Mother, Father) VALUES ('.', 0, '.', '.', '0', '0', '0');")

    database.commit()
