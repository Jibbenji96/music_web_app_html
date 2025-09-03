from lib.artists_repository import ArtistRepository
from lib.artist import Artist

def test_artist_repository_gets_all(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = ArtistRepository(db_connection)

    artists = repo.all()

    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_artist_adds_artist(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = ArtistRepository(db_connection)

    repo.add_artist("Wild nothing", "Indie")

    assert repo.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
    ]


def test_artist_finds_artist(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = ArtistRepository(db_connection)

    assert repo.find_artist(1) == Artist(
        1,
        'Pixies',
        'Rock'
    )
