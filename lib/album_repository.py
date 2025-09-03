from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT "
            "albums.id, "
            "albums.title,"
            "albums.release_year, "
            "albums.artist_id, "
            "artists.name AS artist_name "
            "FROM albums "
            "JOIN artists ON albums.artist_id = artists.id;"
        )

        albums = []
        for row in rows:
            item = Album(
                row["id"],
                row["title"],
                row["release_year"],
                row["artist_id"],
                row["artist_name"]
            )
            albums.append(item)
        
        return albums
    
    def create_album(self, title, release_year, artist_id):
        self._connection.execute(
            "INSERT INTO "
            "albums "
            "(title, release_year, artist_id) "
            "VALUES(%s, %s, %s)", [title, release_year, artist_id]
        )

        return f'Album "{title}" added successfully!'
    
    def find_album(self, id):
        rows = self._connection.execute(
            "SELECT "
            "albums.id, "
            "albums.title,"
            "albums.release_year, "
            "albums.artist_id, "
            "artists.name AS artist_name "
            "FROM albums "
            "JOIN artists ON albums.artist_id = artists.id "
            "WHERE albums.id = %s; "
            , [id]
        )
        
        if rows:  
            row = rows[0]
            return Album(
                    row["id"],
                    row["title"],
                    row["release_year"],
                    row["artist_id"],
                    row["artist_name"]
            )
        return None
    
    def find_by_artist(self, artist_id):
        rows = self._connection.execute(
            "SELECT "
            "* "
            "FROM albums "
            "WHERE artist_id = %s; "
            , [artist_id]
        )

        
        albums = []
        for row in rows:
            album = Album(
                row["id"],
                row["title"],
                row["release_year"],
                row["artist_id"]
            )
            albums.append(album)

        return albums 
    
    
    def get_artist_name(self, artist_id):
        rows = self._connection.execute(
            "SELECT "
            "name "
            "FROM "
            "artists "
            "WHERE id = %s", [artist_id]
        )

        row = rows[0]["name"]

        return str(row)