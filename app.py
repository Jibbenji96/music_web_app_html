import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artists_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/get-specified-album/<id>', methods = ['GET'])
def get_specified_album(id):
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album = album_repo.find_album(id)

    if album is None:
        return "Album not found.", 404  

    return render_template('albums/show.html', album=album)
    
    

@app.route('/get-albums-by-artist/<artist_id>', methods = ['GET'])
def get_albums_by_artist(artist_id):
    connection = get_flask_database_connection(app)
    albums_repo = AlbumRepository(connection)
    albums = albums_repo.find_by_artist(artist_id)
    artist_name = albums_repo.get_artist_name(artist_id)
    
    if albums is None or artist_name is None:
        return "No Albums by this artist", 404
    
    return render_template('artists/index_artist.html', albums=albums, artist_name=artist_name)



@app.route('/get-albums', methods = ['GET'])
def get_albumsl():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()

    if albums is None:
        return "No Albums found.", 404  

    return render_template('albums/index.html', albums=albums)
    


@app.route('/get-specified-artist/<id>', methods = ['GET'])
def get_specified_artist(id):
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artist = artist_repo.find_artist(id)

    if artist is None:
        return "Artist not found.", 404  

    return render_template('artists/show.html', artist=artist)
    


@app.route('/get-artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.all()

    if artists is None:
        return "No Artists found.", 404  

    return render_template('artists/index.html', artists=artists)



"""
@app.route('/get-albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.get_albums()

    formatted_albums = []
    for album in albums:
        formatted_albums.append(f"Album: {album.title}, Release year: {album.release_year}")
    
    return ",\n".join(formatted_albums)
    

@app.route('/add-album', methods = ['POST'])
def create_album():
    
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    repo.create_album(title, release_year, artist_id)

    return f'Album "{title}" added successfully!'


@app.route('/get-artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()

    formatted_artists = []
    for artist in artists:
        formatted_artists.append(f"{artist.name}")
    return ", ".join(formatted_artists)


@app.route('/add-artists', methods = ['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    name = request.form['name'].strip()
    genre = request.form['genre'].strip()

    if name == "" or genre == "":
    
        return 'Please provide an artist name and a genre', 400

    else: 
        repo = ArtistRepository(connection)
        repo.add_artist(name, genre)
        return f'Artist "{name}" added successfully!'
"""

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
