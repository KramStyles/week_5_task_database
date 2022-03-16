from models.song import Song
from models.user import User
from second import Crud, Queries


class Run:
    def __init__(self):
        self.User = User()
        self.Song = Song()

        self.query = Queries()
        self.crud = Crud()

        self.start()

    def run_user(self):
        print(self.User.all(), '\n')
        print(self.User.get(7), '\n')
        print(self.User.create(first_name='michael', last_name='jamie', username='koli'), '\n')
        print(self.User.destroy(3), '\n')
        print(self.User.update(5, username='Hakeem'), '\n')

    def run_songs(self):
        print(self.Song.all(5), '\n')
        print(self.Song.get(3), '\n')
        print(self.Song.create(user_id=5, name='(Finesse) Pheelz & Buju', genre='afro'), '\n')
        print(self.Song.destroy(8), '\n')
        print(self.Song.update(2, True, genre='afro pop'), '\n')

    def run_queries(self):
        print(self.query.passed_students(), '\n')
        print(self.query.failed_students(), '\n')
        print(self.query.test_1_over_45(), '\n')

    def run_crud(self):
        print(self.crud.create("'Jamie', 'Michael', '33211AB', 100, 89.5, 93.7, 95, 93.5, 'A'"), '\n')
        print(self.crud.delete('last_name = "Adam"'), '\n')
        print(self.crud.read(what='first_name', conditions='where Grade = "C"'), '\n')
        print(self.crud.update("last_name='Adama Brand'", condition="first_name='Stern'"), '\n')

    def start(self):
        self.run_user()
        self.run_songs()
        self.run_crud()
        self.run_queries()

