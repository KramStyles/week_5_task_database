from datetime import datetime

from psycopg2 import Error

from models.connection import Connection


class Song(Connection):
    def all(self, user_id=None):
        if user_id and isinstance(user_id, int):
            try:
                self.connect()
                sql = f"""SELECT * FROM songs where user_id = {user_id}"""
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                
                return result if result != [] else None
            except (Exception, Error) as err:
                return f"Fetch All Error: {err}"
            finally:
                self.close_connection()
        else:
            return 'User ID needed'

    def get(self, _id=None):
        pass
