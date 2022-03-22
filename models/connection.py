import psycopg2
import os


class Connection:
    def __init__(self):
        self.conn = self.cursor = None
        self.populate_table()

    def populate_table(self):
        schema = os.getcwd() + '/schema.sql'
        seeder = os.getcwd() + '/seeder.sql'
        self.connect()
        try:
            with open(schema) as file:
                self.cursor.execute(file.read())
                self.conn.commit()
            with open(seeder) as file:
                self.cursor.execute(file.read())
                self.conn.commit()
        except Exception as err:
            return err
        finally:
            self.close_connection()

    def connect(self):
        self.conn = psycopg2.connect(
            user='postgres', password='*',
            port=5432, host='localhost',
            database='db_decagon'
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn: self.conn.close()
        if self.cursor: self.cursor.close()

    @staticmethod
    def verify_input(num):
        if num and isinstance(num, int):
            return num
        if str(num).isdigit():
            return int(num)
        return None
