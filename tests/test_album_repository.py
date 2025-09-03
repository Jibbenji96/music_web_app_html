from lib.album_repository import AlbumRepository
from lib.album import Album

def test_album_repository_returns_albums(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo = AlbumRepository(db_connection)

    albums = repo.all()

    assert albums == [
        Album(1, "Doolittle", 1989, 1, "Pixies"),
        Album(2, "Surfer Rosa", 1988, 1, "Pixies"),
        Album(3, "Waterloo", 1974, 2, "ABBA")
    ]


def test_album_repository_create_album(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo = AlbumRepository(db_connection)

    repo.create_album('Voyage', 2022, 3)

    assert repo.all() == [
        Album(1, "Doolittle", 1989, 1, "Pixies"),
        Album(2, "Surfer Rosa", 1988, 1, "Pixies"),
        Album(3, "Waterloo", 1974, 2, "ABBA"),
        Album(4, "Voyage", 2022, 3, "Taylor Swift")
    ]

def test_album_repository_finds_album(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo =AlbumRepository(db_connection)

    album = repo.find_album(1)

    assert album == Album(1, "Doolittle", 1989, 1, "Pixies")


def test_album_repository_finds_album2(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo =AlbumRepository(db_connection)

    album = repo.find_album(3)

    assert album == Album(3, "Waterloo", 1974, 2, "ABBA")    


def test_album_repository_find_by_artist(db_connection):
    db_connection.seed('seeds/albums_table.sql')

    repo = AlbumRepository(db_connection)

    albums_by_artist = repo.find_by_artist(2)

    assert albums_by_artist == [Album(3, "Waterloo", 1974, 2)]


def test_album_repository_gets_artist_name(db_connection):
    db_connection.seed('seeds/albums_table.sql')

    repo = AlbumRepository(db_connection)

    artist_name = repo.get_artist_name(2)
    
    assert artist_name == "ABBA"