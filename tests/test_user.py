import unittest

from psycopg2 import errors

from models import user


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = user.User()
        self.user.connect()

    def test_to_select_all_data(self):
        self.assertIsNotNone(self.user.all())
        self.assertIsInstance(self.user.all(), list)

    def test_to_get_user_by_id(self):
        self.assertIsNotNone(self.user.get(1))
        self.assertIsNone(self.user.get(19983))
        self.assertIsInstance(self.user.get(2), tuple)
        self.assertEqual(self.user.get('hello'), 'Only Numbers are allowed')

    def test_to_create_user(self):
        self.assertEqual(self.user.create(True, first_name='michael', last_name='jamie', username='koli'), 'Created successfully')
        self.assertIsInstance(self.user.create(True, first_name='michael', last_name='jamie'), str)
        self.assertEqual(self.user.create(), 'Incorrect parameters')

    def tearDown(self) -> None:
        self.user.close_connection()
        self.user = None
