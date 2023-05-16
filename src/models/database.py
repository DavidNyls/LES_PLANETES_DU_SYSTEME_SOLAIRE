import sqlite3
import unittest

class database():
    def __init__(self):
        self.db = sqlite3.connect("projet.db")

    def execute(self, query, params=None):
        if params:
            return self.db.execute(query, params)
        else:
            return self.db.execute(query)

    def setup(self):
        self.execute("CREATE TABLE users (uid INTEGER Primary key UNIQUE, email VARCHAR UNIQUE, password VARCHAR)")
        self.execute("INSERT INTO users (email,password) VALUES ('admin', 'aeadd64d34c8cdbdb0594366c811a803e7df4ad791f96c3190a39d86faff7c9b')")
        self.commit()

    def drop(self):
        self.execute("DROP TABLE IF EXISTS users")

    def commit(self):
        return self.db.commit()