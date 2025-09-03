from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection    

    def all(self):
        rows = self._connection.execute(
            "SELECT "
            "* "
            "FROM "
            "artists; "
        ) 

        artists = []
        for row in rows:
            item = Artist(
                row["id"],
                row["name"],
                row["genre"]
            )

            artists.append(item)

        return artists
    
    def add_artist(self, title, genre):
        self._connection.execute(
            "INSERT INTO "
            "artists "
            "(name, genre) "
            "VALUES( %s, %s)", [title, genre]
        )
        
        return f"{title} added successfully!"
    

    def find_artist(self, id):
        rows = self._connection.execute(
            "SELECT "
            "* "
            "FROM "
            "artists "
            "WHERE id = %s", [id]
        )

        row = rows[0]

        return Artist(
            row["id"],
            row["name"],
            row["genre"]
        )