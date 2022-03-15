import sqlite3
from sqlite3 import Error


class Connection:
    def __init__(self):
        self.conn = self.cursor = None

    def connect(self):
        try:
            # create a connection
            self.conn = sqlite3.connect('gradedb.sqlite', check_same_thread=False)
            self.cursor = self.conn.cursor()
            return 'Done'
        except FileNotFoundError:
            return 'The file is missing'
        except IOError:
            return 'IO Error occurred. File cannot be accessed'

    def close_connection(self):
        if self.conn: self.conn.close()


class Crud(Connection):
    def __init__(self):
        super(Crud, self).__init__()
        self.transfer_data()

    def create_table(self, testing=False):
        sql = """
        Drop table if exists grades;
        create table grades
            (
                id         integer
                    constraint grades_pk
                        primary key autoincrement,
                Last_name  varchar(50) not null,
                First_name varchar(50) not null,
                SSN        varchar(50) not null,
                Test1      int(3),
                Test2      int(3),
                Test3      int(3),
                Test4      int(3),
                Final      int(3),
                Grade      var(2) not null
            );
        """
        conn = self.connect()
        if conn == 'Done':
            try:
                self.cursor.executescript(sql)
                self.conn.commit()
                return 'Done'
            except (Exception, Error) as err:
                return f'Truncate Error {err}'
        return conn

    def transfer_data(self):
        try:
            with open('grades.csv') as file:
                truncate = self.create_table()
                if truncate == 'Done':
                    for item, records in enumerate(file):
                        if item == 0:
                            values = records.replace(' ', '_')
                        else:
                            # Go through records and put string characters into quotes
                            records = [int(x) if x.isdigit() else f'{x.strip()}' for x in records.split(',')]

                            # Convert to string and remove the opening and closing block brackets
                            records = str(records)[1:-1]
                            sql = f"""INSERT INTO grades ({values}) VALUES ({records})"""
                            self.cursor.execute(sql)
                            self.conn.commit()

                    return 'Grades table populated'
                else:
                    return truncate
        except (Exception, Error) as err:
            return f'Error Occurred {err}'
        finally:
            self.close_connection()
