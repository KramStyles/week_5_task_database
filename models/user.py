import psycopg2
import psycopg2.errors


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
        except (Exception, psycopg2.errors) as err:
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
            except (Exception, psycopg2.errors) as err:
                return f"Fetch by ID Error: {err}"
            finally:
                self.close_connection()
        return "Only Numbers are allowed"


