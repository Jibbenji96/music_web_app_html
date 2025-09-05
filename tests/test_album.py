from lib.album import Album

def test_album_constructs():
    voyage = Album(1, 'Voyage', 2022, 2)

    assert voyage.title == 'Voyage'
    assert voyage.release_year == 2022
    assert voyage.artist_id == 2


def test_album_is_valid():
    no_album_title = Album(1, '', 2022, 2)
    no_album_release_year = Album(1, "Voyage", '', 2)
    no_album_artist_id = Album(1, 'Voyage', 2022, None)
    voyage = Album(1, 'Voyage', 2022, 2)

    assert no_album_title.is_valid() == False
    assert no_album_release_year.is_valid() == False
    assert no_album_artist_id.is_valid() == False
    assert voyage.is_valid() == True


def test_album_contains_title_error():
    no_album_name = Album(1, '', 2022, 2)

    assert no_album_name.contains_errors() == "Album has no title."


def test_album_contains_title_and_release_year_errors():
    no_album_title_release_year = Album(1, '', '', 2)

    assert no_album_title_release_year.contains_errors() == "Album has no title, Album has no release year."
