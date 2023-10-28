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


def check_data(user: User):
    fields_with_conflict = {'uid': user.id}
    if (user['Father'] != ""):

        fathers = get_users_by_name(user['Father'])
        if len(fathers) != 1:

            fields_with_conflict['Father'].append(fathers)

    if (user['Mother'] != ""):

        Mothers = get_users_by_name(user['Mother'])
        if len(Mothers) != 1:

            fields_with_conflict['Mother'].append(Mothers)

    if (user['Spouse'] != ""):

        Spouses = get_users_by_name(user['Spouse'])
        if len(fathers) != 1:

            fields_with_conflict['Spouse'].append(Spouses)

    return fields_with_conflict


def convert_to_id(user: User2):

    newUser = User(id=user.id, name=user.name, age=user.name, Birthday=user.Birthday,
                   DeathDate=user.DeathDate, Spouse=user.Spouse, Mother=user.Mother, Father=user.Father)
    if (user.Spouse != ""):

        newUser.Spouse = int(get_users_by_name(user.Spouse).id)
    if (user.Mother != ""):

        newUser.Mother = int(get_users_by_name(user.Mother).id)
    if (user.Father != ""):

        newUser.Father = int(get_users_by_name(user.Father).id)
    return newUser


def update_full(user: User):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET name = '{user.name}', age = {int(user.age)}, Birthday = '{user.Birthday}', DeathDate = '{user.DeathDate}', Spouse = '{user.Spouse}', Mother = {int(user.Mother)}, Father = {int(user.Father)} WHERE uid = {user.id};")
    database.commit()
    print(user)


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


def update_Spouse(Spouse: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET Spouse = '{Spouse}' WHERE uid = {uid};")
    database.commit()


def update_Mother(Mother: int, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET Mother = '{Mother}' WHERE uid = '{uid}';")
    database.commit()


def update_Father(Father: int, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET Father = '{Father}' WHERE uid = '{uid}';")
    database.commit()


def remove_user(uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"DELETE FROM users WHERE uid = '{uid}'")
    database.commit()
