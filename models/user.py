from datetime import datetime

import psycopg2
from psycopg2 import OperationalError, errors, errorcodes


class User:
    def __init__(self):
        self.conn = self.cursor = None

    def connect(self):
        self.conn = psycopg2.connect(
            user='postgres', password='*',
            host='localhost', port=5432,
            database='db_decagon'
        )

        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.conn.close()
        if self.cursor:
            self.cursor.close()

    def all(self):
        try:
            self.connect()
            sql = """SELECT * FROM users"""
            self.cursor.execute(sql)

            return self.cursor.fetchall()
        except (Exception, errors) as err:
            return f"Fetch All Error: {err}"
        finally:
            self.close_connection()

    def get(self, _id: int):
        if _id and isinstance(_id, int):
            try:
                self.connect()
                sql = f"""SELECT * FROM users where id = {_id}"""
                self.cursor.execute(sql)

                return self.cursor.fetchone()
            except errors as err:
                return f"Fetch by ID Error: {err}"
            finally:
                self.close_connection()
        return "Only Numbers are allowed"

    # def db_operations(function):
    #     def wrapper(self, **params):
    #         try:
    #             self.connect()
    #             return function(**params)
    #         except Exception as err:
    #             return f'Database Operational Error: {err}'
    #         finally:
    #             self.close_connection()
    #
    #     return wrapper()

    # @db_operations
    def create(self, testing=False, **params):
        if params:
            try:
                self.connect()
                params['created_at'] = datetime.today().strftime("%Y-%m-%d")
                columns = ', '.join(params.keys())
                values = str(list(params.values())).replace('[', '').replace(']', '')
                sql = f"""INSERT INTO users ({columns}) values ({values})"""

                self.cursor.execute(sql)
                if not testing:
                    self.conn.commit()
                return 'Created successfully'
            except Exception as err:
                return f'Create User Error: {err}'
            finally:
                self.close_connection()
        else:
            return 'Incorrect parameters'


# print(User().create(username='folukotibo', first_name='Folusho', last_name='kotibo'))
