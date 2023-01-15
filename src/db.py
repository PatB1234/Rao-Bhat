import time
from pydantic import BaseModel
from jose import jwt, JWTError
import os
from passlib.context import CryptContext
from datetime import date, datetime, timedelta
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


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
        
        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:

                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["id"]])
        return arr

driver = App("neo4j+s://7fac8116.databases.neo4j.io", "neo4j", "RSV5Kinf7IS6yjkeHS6IepdROANLalVWENFAD0gJSmU")


def get_tree():

    return driver.run_command("""MATCH (p: Person) RETURN p.marraige AS marraige, p.name AS name, p.born AS born, p.died AS died, p.place AS place, ID(p) AS id""")

driver.close()