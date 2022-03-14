import unittest

from psycopg2 import Error

from models import song


class TestSong(unittest.TestCase):
    def setUp(self) -> None:
        self.song = song.Song()

    def test_to_select_all_songs_from_a_user(self):
        self.assertIsNotNone(self.song.all(3))
        self.assertIsNone(self.song.all(4))
        self.assertIsInstance(self.song.all(5), list)
        self.assertEqual(self.song.all(), 'User ID needed')

    def test_to_create_songs(self):
        self.assertEqual(self.song.create())

    def tearDown(self) -> None:
        self.song.close_connection()
        self.song = None
