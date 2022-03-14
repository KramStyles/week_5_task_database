import unittest
import datetime
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

    def test_to_get_one_song(self):
        self.assertIsNotNone(self.song.get(1))
        self.assertIsNone(self.song.get(1239983))
        self.assertIsInstance(self.song.get(4), tuple)
        self.assertEqual(self.song.get('1'), (1, 3, '(So bad) Joe boy ft Simi', 'afro', datetime.date(2021, 3, 14), None))
        self.assertEqual(self.song.get('one dance'), 'Only Numbers are allowed')

    def test_to_create_songs(self):
        self.assertEqual(self.song.create(True, user_id=3, name='(Finesse) Pheelz & Buju', genre='afro'), 'Song added')
        self.assertIsInstance(self.song.create(True, user_id=322, name='(Ginger Me) Rema', genre='afro'), Error)
        self.assertEqual(self.song.create(), 'Incorrect parameters')
        self.assertIsInstance(self.song.create(True, first_name='michael', last_name='jamie'), Error)

    def tearDown(self) -> None:
        self.song.close_connection()
        self.song = None
