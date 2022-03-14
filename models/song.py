from datetime import datetime

import psycopg2
from psycopg2 import Error


class Song:
    def __init__(self):
        self.conn = psycopg2.connect(
            user='postgres', password='*',
            port=5432, host='localhost',
            database='db_decagon'
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn: self.conn.close()
        if self.cursor: self.cursor.close()

    def all(self, user_id=None, testing=False):
        pass
