import time
from pydantic import BaseModel
from jose import jwt, JWTError
import os
from passlib.context import CryptContext
from datetime import date, datetime, timedelta
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

def deduplicate_by_ip(a):


    source_ips = []
    new_list = []
    for i in range(len(a)):
        if a[i][0] != None:
            if a[i][0] not in source_ips:
                source_ips.append(a[i][0])
                new_list.append(a[i])
    return new_list

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    @staticmethod
    def _run_command(tx, command):

        result = tx.run(command)
        entire_result = [] # Will contain all the items
        for record in result:
            entire_result.append(record)
        
        return entire_result

    def run_command(self, command):

        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)

            return res
    
    def get_nodes(self, command):
        
        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:
                
                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["id"], line["id2"], line["id3"]])

        return deduplicate_by_ip(arr)
    def test(self, command):
        
        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:
                
                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["ID"], line["PID"]])

        return deduplicate_by_ip(arr)
    def get_married_nodes(self, command):

        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:
                
                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["id"], line["id2"], line["PID"]])

        return deduplicate_by_ip(arr)

    def delete_temp_nodes(self):

        with self.driver.session() as session:
            res = session.execute_write(self._run_command, "MATCH (t: TempNode) DELETE (t)")

    def non_married(self, command) :

        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:

                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["parents"], line["id"], line["gender"]])

        return arr

    def add_member(self, name, mid, fid, pid, gender, married, place):

        with self.driver.session() as session:
            
            jsonData = f'name: "{name}", gender: "{gender}", marraige: {married}, parents: ["{mid}", "{fid}"], marriedTo: ["{pid}"], place: "{place}"'
            session = session.execute_write(self._run_command, "CREATE (p: Person {" + jsonData + "}) RETURN ID(p) AS id")
            for line in session:

                return line["id"]

    def married(self, command) :

        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:

                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["parents"], line["marriedTo"], line["id"], line["gender"]])
        
        return arr
driver = App("neo4j+s://f5963dab.databases.neo4j.io", "neo4j", "3PdgWqKy110mz3ztpK37BdSOj89fsRUrUJ79cRyXcxU")

def edit_node(ids, gender, name, marriedTo, mid, fid, place, marraige):

    driver.run_command(f"MATCH (p: Person WHERE ID(p) = {ids}) SET p.gender = '{gender}', p.name = '{name}', p.marriedTo = {[marriedTo]}, p.parents = ['{mid}', '{fid}'], p.place = '{place}', p.marraige = {marraige}")

def add_human(name, mid, fid, pid, gender, married, place):

    return driver.add_member(name, mid, fid, pid, gender, married, place)

def get_tree():

    fixedArr = []

    a_non = driver.non_married("MATCH (p: Person) WHERE p.marraige = False RETURN p.name AS name, toString(p.born) AS born, toString(p.died) AS died, p.place AS place, p.marraige AS marraige, p.parents AS parents, ID(p) AS id, p.gender AS gender")
    fA1 = []

    for data in a_non:
        print(data)
        if (data[5] == None or data[6] == None):
            
            fA1.append(data)
        else:

            tFid = data[5][0]
            tMid = data[5][1]

            if (data[5][0] == None or data[5][1] == None):

                tMid = None
                tFid = None

                fA1.append([data[0], data[1], data[2], data[3], None, None, data[6], data[7]])
            else:

                fA1.append([data[0], data[1], data[2], data[3], None, [tMid, tFid], data[6], data[7]])




    for data in fA1:


        # if (data[2] == None):

        if (data[5] == "None" or data[5] == None):
            
            #, "Born": data[1], "Marraige": data[4], 
            fixedArr.append({"id": data[6], "name": data[0], "Place": data[3], "gender": data[7].lower(), "photo": "", "addr": "", "title": f"ID: {data[6]}"})
        else: 

            #, "Born": data[1], "Marraige": data[4], "Place": data[3], 
            print(data)
            fixedArr.append({"id": data[6], "name": data[0], "mid": data[5][0], "fid": data[5][1], "gender": data[7].lower(), "photo": "", "addr": "", "title": f"ID: {data[6]}"})
        # else:

        #     if (data[5] == None):

        #         #, "Born": data[1], "Died": data[2], "Place": data[3], "Marraige": data[4], 
        #         fixedArr.append({"id": data[6], "name": data[0], "gender": data[7].lower(), "photo": "", "addr": ""})
        #     else: 

        #         #, "Born": data[1], "Died": data[2], "Place": data[3], "Marraige": data[4]
        #         fixedArr.append({"id": data[6], "name": data[0], "mid": data[5][0], "fid": data[5][1], "gender": data[7].lower(), "photo": "", "addr": ""})



    b = driver.married("MATCH (p: Person) WHERE p.marraige = True RETURN p.name AS name, toString(p.born) AS born, toString(p.died) AS died, p.place AS place, p.marraige AS marraige, p.parents AS parents, p.marriedTo AS marriedTo, ID(p) AS id, p.gender AS gender")

    fA2 = []

    for data in b:
        
        print(data)
        if (data[5] == None or data[6] == None):
                        
            fA2.append(data)
        else:

            tFid = data[5][0]
            tMid = data[5][1]
            tPid = data[4]
            if data[4] == ["None"]:
                
                    tPid = None
            if (data[5][0] == None or data[5][1] == None):

                tMid = None
                tFid = None

                fA2.append([data[0], data[1], data[2], data[3], tPid, None, data[6], data[7], data[8]])
            else:

                fA2.append([data[0], data[1], data[2], data[3], tPid, [tMid, tFid], data[6], data[7], data[8]])


    for data in fA2:

        # if (data[2] == None):

        if (data[5] == "None" or data[5] == None):

            #, "Born": data[1], "Place": data[3], "Marraige": data[4]
            fixedArr.append({"id": data[7], "name": data[0], "pid": data[6][0], "gender": data[8].lower(), "photo": "", "addr": "", "title": f"ID: {data[7]}"})
        else: 

            #, "Born": data[1], "Place": data[3], "Marraige": data[4] 
            print(data)
            fixedArr.append({"id": data[7], "name": data[0], "mid": data[5][0], "fid": data[5][1], "pid": data[6][0], "gender": data[8].lower(), "photo": "", "addr": "", "title": f"ID: {data[7]}"})
    # else:

        #     if (data[5] == None):

        #         #, "Born": data[1], "Died": data[2], "Place": data[3], "Marraige": data[4]
        #         fixedArr.append({"id": data[7], "name": data[0], "pid": data[6][0], "gender": data[8].lower(), "photo": "", "addr": ""})
        #     else: 

        #         #, "Born": data[1], "Died": data[2], "Place": data[3], "Marraige": data[4],
        #         fixedArr.append({"id": data[7], "name": data[0], "mid": data[5][0], "fid": data[5][1], "pid": data[6][0], "gender": data[8].lower(), "photo": "", "addr": ""})

    return fixedArr


driver.close()

print(get_tree())