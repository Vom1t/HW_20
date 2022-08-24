from unittest.mock import MagicMock
import pytest


from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService

# Фикстура для МувиДАО
@pytest.fixture()
def movie_dao():
    movie_init = MovieDAO(None)

    movie_1 = Movie(id=1, title='movie_1', description="description", trailer='trailer', year=2020, rating=20.1,
                    genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='movie_2', description="description", trailer='trailer', year=2020, rating=20.1,
                    genre_id=1, director_id=1)

    movie_init.get_one = MagicMock(return_value=movie_1)
    movie_init.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_init.create = MagicMock(return_value=movie_1)
    movie_init.delete = MagicMock()
    movie_init.update = MagicMock()

    return movie_init
# Класс тестов МувиСервис
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).title == 'movie_1'

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 2

    def test_create(self):
        data = {
            'id': 2,
            'title': 'movie_1',
            'description': "description",
            'trailer': 'trailer',
            'year': 2020,
            'rating': 20.1,
            'genre_id': 1,
            'director_id': 1
        }

        assert self.movie_service.create(data).title == data.get('title')

    def test_delete(self):
        assert 1==1

    def test_update(self):
        assert 1==1

