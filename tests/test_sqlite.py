import unittest
from sqlite3 import Error

from second import Connection, Crud


class TestConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = Connection()

    def test_connection(self):
        self.assertEqual(self.conn.connect(), 'Done')

    def tearDown(self) -> None:
        self.conn = None


class TestCreateTable(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = Crud()

    def test_to_create_table(self):
        self.assertEqual(self.conn.create_table(), 'Done')

    def test_to_populate_table(self):
        self.assertEqual(self.conn.transfer_data(), 'Grades table populated')

    def tearDown(self) -> None:
        self.conn = None


if __name__ == '__main__':
    unittest.main()
