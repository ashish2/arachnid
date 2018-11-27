from config import *

class DBConn(object):
    def __init__(self, conn):
        "Make DB Connections to the specified DB"
       self.conn = conn



db = DBConn()
#print(db)

