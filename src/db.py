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


    def get_nodes(self, command):
        
        arr = []
        with self.driver.session() as session:
            res = session.execute_write(self._run_command, command)
            for line in res:
                
                arr.append([line["name"], line["born"], line["died"], line["place"], line["marraige"], line["id"], line["id2"], line["id3"]])

        return deduplicate_by_ip(arr)

driver = App("neo4j+s://7fac8116.databases.neo4j.io", "neo4j", "RSV5Kinf7IS6yjkeHS6IepdROANLalVWENFAD0gJSmU")


def get_tree():

    a = driver.get_nodes("MATCH (p: Person) MATCH (p)-[:CHILD_OF]->(p2: Person) MATCH (p)-[:CHILD_OF]->(p3: Person) RETURN p.marraige AS marraige, p.name AS name, p.born AS born, p.died AS died, p.place AS place, ID(p) AS id, ID(p2) AS id2, ID(p3) AS id3")

    b = driver.get_nodes("MATCH (p: Person) MATCH (p)<-[:CHILD_OF]-(p2: Person) MATCH (p)<-[:CHILD_OF]-(p3: Person) RETURN p.marraige AS marraige, p.name AS name, p.born AS born, p.died AS died, p.place AS place, ID(p) AS id, ID(p2) AS id2, ID(p3) AS id3")

    comb = a + b
    comb = deduplicate_by_ip(comb)
    return comb
driver.close()

print(get_tree())