from lib.artist import Artist

def test_artist_constructs():
    artist = Artist('Wild nothing', 'Indie')

    assert artist.name == 'Wild nothing'
    assert artist.genre == 'Indie'

def test_artist_contents():
    artist = Artist('Wild nothing', 'Indie')
    artist1 = Artist('Wild nothing', 'Indie')

    assert artist == artist1

def test_artist_formats():
    artist = Artist('Wild nothing', 'Indie')

    assert str(artist) == 'Artist(Wild nothing, Indie)'