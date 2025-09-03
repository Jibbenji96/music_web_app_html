from lib.album import Album

def test_album_constructs():
    voyage = Album(1, 'Voyage', 2022, 2)

    assert voyage.title == 'Voyage'
    assert voyage.release_year == 2022
    assert voyage.artist_id == 2