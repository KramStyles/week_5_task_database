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


class TestCrud(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Crud()

    def test_to_create_data(self):
        self.assertEqual(self.db.create("'Jamie', 'Michael', '33211AB', 100, 89.5, 93.7, 95, 93.5, 'A'"), 'ok')
        self.assertIsInstance(self.db.create("'Jamie', 'Michael', '33211AB', 100, 89.5, 93.7, 95, 93.5"), Error)
        self.assertIsInstance(self.db.create(columns='last_name, first_name, ssn, grade', data="'Dec', 'Agon', '33443', 'E'"), str)

    def test_to_read_data(self):
        self.assertEqual(self.db.read(what='first_name', conditions='where Grade = "C"'),  [('Hernandez',), ('Payton',)])
        self.assertIsInstance(self.db.read(what='first_name', conditions='where Grade = "C"'), list)
        self.assertIsInstance(self.db.read(what='firstname', conditions='where Grade = "C"'), Error)

    def test_to_update_data(self):
        self.assertEqual(self.db.update("last_name='Adama Brand'", condition="first_name='Stern'"), 'ok')
        self.assertIsInstance(self.db.update("lastname='Adama Brand'", condition="first_name='Stern'"), Error)

    def test_to_delete_data(self):
        self.assertEqual(self.db.delete('last_name = "Adam"'), 'ok')
        self.assertIsInstance(self.db.delete('firstname = Jerry'), Error)

    def tearDown(self) -> None:
        self.db = None


if __name__ == '__main__':
    unittest.main()
    # python -m unittest tests/test_sqlite.py -v