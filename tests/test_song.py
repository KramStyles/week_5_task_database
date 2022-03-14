import unittest

from psycopg2 import Error

from models import song


class TestSong(unittest.TestCase):
    def setUp(self) -> None:
        self.song = song.Song()

    def test_to_select_all_songs_from_a_user(self):
        # self.assertIsNotNone(self.song.all(1))
        # self.assertIsInstance(self.song.all(2), list)
        self.assertEqual(self.song.all(), 'User ID needed')

    def tearDown(self) -> None:
        self.song.close_connection()
        self.song = None
