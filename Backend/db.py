from pydantic import BaseModel
import os
import sqlite3 as driver


DATABASE_URL = 'Backend/db/users.db'


class User(BaseModel):

    uid: int
    name: str
    age: int
    birthday: str
    deathDate: str
    pids: list[int] = []
    mid: int
    fid: int


def create_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (uid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INT, birthday TEXT, deathDate TEXT, pids VARCHAR, mid INT, fid INT);")


def create_user(name: str, age: str, birthday: str, deathDate: str, pids: list[int], mid: int, fid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    arr = ','.join([str(x) for x in pids])
    cursor.execute(
        f"INSERT INTO users (name, age, birthday, deathDate, pids, mid, fid) VALUES ('{name}', '{age}', '{birthday}', '{deathDate}', '{arr}', '{mid}', '{fid}');")

    database.commit()


def get_all_users():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    database.commit()
    userForm = []

    for user in users:
        string = user[5].split(',')
        userForm.append(User(uid=user[0], name=user[1], age=user[2], birthday=user[3],
                        deathDate=user[4], pids=string, mid=user[6], fid=user[7]))
    return userForm


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


def update_birthday(birthday: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET birthday = '{birthday}' WHERE uid = {uid};")
    database.commit()


def update_deathDate(deathDate: str, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET deathDate = '{deathDate}' WHERE uid = {uid};")
    database.commit()


def update_pids(pids: list[int], uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET pids = '{','.join([str(x) for x in pids])}' WHERE uid = {uid};")
    database.commit()


def update_mid(mid: int, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET mid = '{mid}' WHERE uid = '{uid}';")
    database.commit()


def update_fid(fid: int, uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(
        f"UPDATE users SET fid = '{fid}' WHERE uid = '{uid}';")
    database.commit()


def remove_user(uid: int):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"DELETE FROM users WHERE uid = '{uid}'")
    database.commit()
