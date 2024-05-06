from . import session
from typing import List, Union

class Genre(object):
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    @classmethod
    def from_json(cls, json_data: dict) -> 'Genre':
        """
        Creates a Genre object from JSON data.
        """
        return cls(json_data['id'], json_data['name'])


    @staticmethod
    def list(type: str = 'movie', is_raw: bool = False, params: dict = {}) -> Union[List['Genre'], dict]:
        """
        Retrieves a list of Genre objects from an API.
        """

        path = 'https://api.themoviedb.org/3/genre/{}/list'.format(type)

        response = session.get(path, params=params)
        json_data = response.json()

        if is_raw:
            return json_data

        # Extract genres from the JSON response and convert them to Genre objects
        genres = [Genre.from_json(genre_data) for genre_data in json_data['genres']]

        return genres


