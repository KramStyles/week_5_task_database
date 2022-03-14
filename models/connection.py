import psycopg2


class Connection:
    def __init__(self):
        self.conn = self.cursor = None

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
