from datetime import datetime

import psycopg2
from psycopg2 import Error

from models.connection import Connection


class Song(Connection):
    def all(self, user_id=None):
        if user_id and isinstance(user_id, int):
            try:
                self.connect()
                sql = """SELECT * FROM songs"""
                self.cursor.execute(sql)

                return self.cursor.fetchall()
            except (Exception, Error) as err:
                return f"Fetch All Error: {err}"
            finally:
                self.close_connection()
        else:
            return 'User ID needed'
