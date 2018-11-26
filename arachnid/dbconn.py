from config import *

class DBConn(object):
    def __init__(self, conn):
        "Make DB Connections to the specified DB"
        self. conn = conn

    def __del__(self):
        "Clean all DBConn's"
        self.j = 3


db = DBConn()
print(db)

