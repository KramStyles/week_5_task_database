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
            return f"Something went wrong: {err}"
        finally:
            self.close_connection()


