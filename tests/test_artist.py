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