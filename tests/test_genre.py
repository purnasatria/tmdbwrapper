import vcr
from pytest import fixture
from tmdbwrapper import Genre

@fixture
def genre_keys():
    return ['id', 'name']

def test_from_json():
    # Create a sample genre dictionary
    genre_data = {'id': 28, 'name': 'Action'}

    # Call the from_json method
    genre = Genre.from_json(genre_data)

    # Check if the genre is an instance of Genre class
    assert isinstance(genre, Genre)

    # Check if the genre attributes are correct
    assert genre.id == 28
    assert genre.name == 'Action'


@vcr.use_cassette('tests/vcr_cassettes/genre-movie.yml', filter_query_parameters=['api_key'])
def test_genre_list_movie():
    genres = Genre.list()

    # Check if the list contains the expected number of genres
    assert len(genres) > 0

    # Check if the genres are instances of Genre class
    assert all(isinstance(genre, Genre) for genre in genres)

@vcr.use_cassette('tests/vcr_cassettes/genre-movie.yml', filter_query_parameters=['api_key'])
def test_genre_list_movie_raw(genre_keys):
    response = Genre.list(is_raw=True)

    assert isinstance(response, dict)
    assert isinstance(response['genres'], list)
    assert isinstance(response['genres'][0], dict)
    assert set(genre_keys).issubset(response['genres'][0].keys())


@vcr.use_cassette('tests/vcr_cassettes/genre-tv.yml', filter_query_parameters=['api_key'])
def test_genre_list_tv():
    genres = Genre.list(type='tv')

    # Check if the list contains the expected number of genres
    assert len(genres) > 0

    # Check if the genres are instances of Genre class
    assert all(isinstance(genre, Genre) for genre in genres)

@vcr.use_cassette('tests/vcr_cassettes/genre-tv.yml', filter_query_parameters=['api_key'])
def test_genre_list_tv_raw(genre_keys):
    response = Genre.list(type='tv', is_raw=True)

    assert isinstance(response, dict)
    assert isinstance(response['genres'], list)
    assert isinstance(response['genres'][0], dict)
    assert set(genre_keys).issubset(response['genres'][0].keys())

@vcr.use_cassette('tests/vcr_cassettes/genre-list-with-param.yml', filter_query_parameters=['api_key'])
def test_genre_list_with_param(genre_keys):
    params = {}
    params['language'] = 'id'
    response = Genre.list(is_raw=True, params=params)

    assert isinstance(response, dict)
    assert isinstance(response['genres'], list)
    assert isinstance(response['genres'][0], dict)
    assert set(genre_keys).issubset(response['genres'][0].keys())

