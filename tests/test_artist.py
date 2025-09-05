from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, 'Wild nothing', 'Indie')

    assert artist.id == 1
    assert artist.name == 'Wild nothing'
    assert artist.genre == 'Indie'

def test_artist_contents():
    artist = Artist(1, 'Wild nothing', 'Indie')
    artist1 = Artist(1, 'Wild nothing', 'Indie')

    assert artist == artist1

def test_artist_formats():
    artist = Artist(1, 'Wild nothing', 'Indie')

    assert str(artist) == 'Artist(1, Wild nothing, Indie)'


def test_artist_is_valid():
    no_artist_name = Artist(1, '', 'Indie')
    no_artist_genre = Artist(2, 'Wild nothing', '')
    artist = Artist(1, 'Wild nothing', 'Indie')

    assert no_artist_name.is_valid() == False
    assert no_artist_genre.is_valid() == False
    assert artist.is_valid() == True


def test_artist_contains_name_error():
    no_artist_name = Artist(1, '', 'Indie')

    assert no_artist_name.contains_errors() == "Artist has no name."


def test_artist_contains_name_and_genre_errors():
    no_artist_name = Artist(1, '', '')

    assert no_artist_name.contains_errors() == "Artist has no name, Artist has no genre."



