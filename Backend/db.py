from pydantic import BaseModel
import os
import sqlite3 as driver
from sqlite3.dbapi2 import Cursor

DATABASE_URL = 'db/users.db'


class User(BaseModel):

    id: int
    name: str
    age: int
    birthday: str
    deathDate: str
    pids: list[int]
    mid: int
    fid: int


def create_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (uid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INT, Birthday TEXT, DeathDate TEXT, pids VARCHAR, Mother INT, Father INT);")


def create_user(name: str, age: int, Birthday: str, DeathDate: str, pids: str, Mother: int, Father: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"INSERT INTO users (name, age, Birthday, DeathDate, pids, Mother, Father) VALUES ('{name}', '{age}', '{Birthday}', '{DeathDate}', '{pids}', '{Mother}', '{Father}');")

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
        userForm.append(User(id=user[0], name=user[1], age=user[2], birthday=user[3],
                        deathDate=user[4], pids=pid, mid=user[6], fid=user[7]))
    return userForm


def update_full(user: User):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET name = '{user.name}', age = {int(user.age)}, Birthday = '{user.Birthday}', DeathDate = '{user.DeathDate}', pids = '{user.pids}', Mother = {int(user.Mother)}, Father = {int(user.Father)} WHERE uid = {user.id};")
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


def update_pids(pids: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET pids = '{pids}' WHERE uid = {uid};")
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
