import unittest

from psycopg2 import Error

from models import user


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = user.User()
        self.user.connect()

    def test_to_select_all_data(self):
        self.assertIsInstance(self.user.all(), list)
        self.assertIsNotNone(self.user.all())

    def test_to_get_user_by_id(self):
        self.assertIsNotNone(self.user.get(3))
        self.assertIsNone(self.user.get(19983))
        self.assertIsInstance(self.user.get(3), tuple)
        self.assertEqual(self.user.get('hello'), 'Only Numbers are allowed')

    def test_to_create_user(self):
        self.assertEqual(self.user.create(True, first_name='michael', last_name='jamie', username='koli'), 'Created successfully')
        self.assertIsInstance(self.user.create(True, first_name='michael', last_name='jamie'), str)
        self.assertEqual(self.user.create(), 'Incorrect parameters')

    def test_to_update_user_record(self):
        self.assertEqual(self.user.update(4, True, username='kelly', last_name='martin'), 'Changes applied!')
        self.assertEqual(self.user.update(), 'Incomplete parameters')
        self.assertIsInstance(self.user.update(1, True, fullname='Jerry Michael'), Error)

    def test_to_delete_user_record(self):
        self.assertEqual(self.user.destroy(), 'Invalid parameters')
        self.assertEqual(self.user.destroy(101, True), 'Record destroyed!')

    def tearDown(self) -> None:
        self.user.close_connection()
        self.user = None
