import unittest

from psycopg2 import Error

from models import song


class TestSong(unittest.TestCase):
    def setUp(self) -> None:
        self.song = song.Song()

    def test_to_select_all_songs_from_a_user(self):
        pass