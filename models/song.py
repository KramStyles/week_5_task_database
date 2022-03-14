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
        if self.verify_input(_id):
            try:
                self.connect()
                sql = f"""SELECT * FROM songs where id = {_id}"""
                self.cursor.execute(sql)

                return self.cursor.fetchone()
            except (Exception, Error) as err:
                return f"Fetch by ID Error: {err}"
            finally:
                self.close_connection()
        return "Only Numbers are allowed"

    def create(self, testing=False, **params):
        if params:
            try:
                self.connect()
                params['created_at'] = datetime.today().strftime("%Y-%m-%d")
                columns = ', '.join(params.keys())
                values = str(list(params.values())).replace('[', '').replace(']', '')
                sql = f"""INSERT INTO songs ({columns}) values ({values})"""

                self.cursor.execute(sql)
                if not testing:
                    self.conn.commit()
                return 'Song added'
            except (Exception, Error) as err:
                return err
            finally:
                self.close_connection()
        else:
            return 'Incorrect parameters'

    def update(self, _id=None, testing=False, **params):
        if self.verify_input(_id):
            try:
                self.connect()

                # Turn the params into a string of arguments
                arguments = ', '.join([f"{x} = '{params[x]}'" for x in params])

                sql = f'UPDATE songs SET {arguments} where id = {_id}'
                self.cursor.execute(sql)
                if not testing:
                    self.conn.commit()
                return 'Record updated!'
            except Error as err:
                return err
            finally:
                self.close_connection()
        else:
            return 'Incomplete parameters'

    def destroy(self, _id=None, testing=False):
        if self.verify_input(_id):
            try:
                self.connect()
                sql = f'DELETE FROM songs where id = {_id}'
                self.cursor.execute(sql)
                if not testing:
                    self.conn.commit()
                return 'Song deleted!'
            except (Exception, Error) as err:
                return err
            finally:
                self.close_connection()
        else:
            return 'Invalid parameters'
