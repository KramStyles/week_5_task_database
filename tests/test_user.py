import unittest
from models import user


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = user.User()
        self.user.connect()

    def test_all(self):
        self.assertIsNotNone(self.user.all())
        self.assertIsInstance(self.user.all(), list)

    def test_get(self):
        self.assertIsNotNone(self.user.get(1))
        self.assertIsNone(self.user.get(19983))
        self.assertIsInstance(self.user.get(2), tuple)
        self.assertEqual(self.user.get('hello'), 'Only Numbers are allowed')

    def tearDown(self) -> None:
        self.user.close_connection()
        self.user = None
