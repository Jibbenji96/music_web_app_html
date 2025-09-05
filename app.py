import os
from flask import Flask, request, render_template, redirect, url_for

from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artists_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/get-albums/create/<int:artist_id>', methods = ['GET'])
def get_new_album(artist_id):
    connection = get_flask_database_connection(app)
    album_repo =AlbumRepository(connection)
    artist_name = album_repo.get_artist_name(artist_id)
    return render_template('artists/new_album.html', artist_id=artist_id, artist_name=artist_name)



@app.route('/get-albums', methods=['POST'])
def post_new_album():
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = int(request.form['artist_id'])
    
    album = Album(None, title, release_year, artist_id)
    
    if not album.is_valid():
        return render_template('artists/new_album.html', errors = album.contains_errors()), 400

    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album_repo.create_album(title, release_year, artist_id)

    return redirect(url_for('get_albums_by_artist', artist_id=artist_id))




@app.route('/get-albums/<int:id>', methods = ['GET'])
def get_specified_album(id):
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album = album_repo.find_album(id)

    if album is None:
        return "Album not found.", 404  

    return render_template('albums/show.html', album=album)
    


@app.route('/get-albums/get-albums-by-artist/<int:artist_id>', methods = ['GET'])
def get_albums_by_artist(artist_id):
    connection = get_flask_database_connection(app)
    albums_repo = AlbumRepository(connection)
    albums = albums_repo.find_by_artist(artist_id)
    artist_name = albums_repo.get_artist_name(artist_id)
    
    if albums is None or artist_name is None:
        return "No Albums by this artist", 404
    
    return render_template('artists/show_artist_albums.html', albums=albums, artist_name=artist_name)



@app.route('/get-albums', methods = ['GET'])
def get_albumsl():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()

    if albums is None:
        return "No Albums found.", 404  

    return render_template('albums/index.html', albums=albums)
    


@app.route('/get-artists/create', methods=['GET'])
def get_new_artist():
    
    return render_template('artists/new_artist.html')



@app.route('/get-artists', methods=['POST'])
def post_new_artist():
    name = request.form['name']
    genre = request.form['genre']

    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artist = Artist(None, name, genre)
    
    if not artist.is_valid():
        return render_template('artists/new_artist.html', errors = artist.contains_errors()), 400

    artist_repo.add_artist(name, genre)


    return redirect(url_for('get_artists'))



@app.route('/get-artists/<int:id>', methods = ['GET'])
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
