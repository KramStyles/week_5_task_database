import unittest
from models import user


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = user.User()
        self.user.connect()

    def test_all(self):
        self.assertIsNotNone(self.user.all())
        self.assertIsInstance(self.user.all(), list)

    def tearDown(self) -> None:
        self.user.close_connection()
        self.user = None
