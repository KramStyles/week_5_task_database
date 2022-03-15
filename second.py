import sqlite3
from sqlite3 import Error


class Connection:
    def __init__(self):
        self.conn = self.cursor = None

    def connect(self):
        pass


class Crud(Connection):
    def __init__(self):
        super(Crud, self).__init__()

    def create_table(self):
        pass

    def transfer_data(self):
        pass
