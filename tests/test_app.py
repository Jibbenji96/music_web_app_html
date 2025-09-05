from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can return the albums from the albums database in a HTML file
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-albums")

    div_tags = page.locator("div")
    
    expected_titles = [
        "Doolittle",
        "Surfer Rosa",
        "Waterloo"
    ]
    for index, title in enumerate(expected_titles):
        expect(div_tags.nth(index)).to_have_text(title)
    

"""
We can return a given album from the albums database, and its artist
from the artist database and return it in an HTML file
"""
def test_get_specified_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-albums/1")

    h1_tag = page.locator("h1")
    p_tags = page.locator("p")

    expect(h1_tag).to_have_text("Doolittle")
    expect(p_tags).to_have_text(
        "Release year: 1989\n" \
        "Artist: Pixies\n\n" \
        "Return to Albums list"
    )

"""
We connect to the main album list, click an album and receive the 
album information in a new page, then return to album list.
"""

def test_get_albums_return_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-albums")

    page.click("a:has-text('Doolittle')")

    p_tags = page.locator("p")

    expect(p_tags).to_have_text(
        "Release year: 1989\nArtist: Pixies\n\nReturn to Albums list")

    page.click("a:has-text('Return to Albums list')")
    
    div_tags = page.locator("div")
    
    expected_titles = [
        "Doolittle",
        "Surfer Rosa",
        "Waterloo"
    ]
    for index, title in enumerate(expected_titles):
        expect(div_tags.nth(index)).to_have_text(title)
    

"""
We access a list of artists from a database using the 
GET artists HTML
"""

def test_get_artists_returns_artist_list(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f'http://{test_web_address}/get-artists')

    div_tags = page.locator("div")
    print(div_tags)
    expected_names = [
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ]
    for index, name in enumerate(expected_names):
        expect(div_tags.nth(index)).to_have_text(name)


"""
We click from artists page to access information on one artist, 
then return to original artists directory page
"""

def test_get_artists_return_artist_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-artists")

    page.click("a:has-text('Pixies')")

    p_tags = page.locator("p")

    expect(p_tags).to_have_text(
        "Albums by Pixies\n\nGenre: Rock\n\nCreate new album by Pixies\n\nReturn to Artists list")

    page.click("a:has-text('Return to Artists list')")
    
    div_tags = page.locator("div")
    
    expected_names = [
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ]
    for index, name in enumerate(expected_names):
        expect(div_tags.nth(index)).to_have_text(name)

"""
We access an artist from the artists list, then click the albums
hyperlink and are shown albums by this artist
"""

def test_artists_to_artist_to_albums_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-artists")

    page.click("a:has-text('Pixies')")

    page.click("a:has-text('Albums by Pixies')")

    strong_tags = page.locator("strong")
    
    expected_titles = [
        "Doolittle",
        "Surfer Rosa"
    ]
    for index, title in enumerate(expected_titles):
        expect(strong_tags.nth(index)).to_have_text(title)
    
    page.click("a:has-text('Return to Artists')")

    div_tags = page.locator("div")
    
    expected_names = [
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ]
    for index, name in enumerate(expected_names):
        expect(div_tags.nth(index)).to_have_text(name)


"""
We navigate from the home page to an artist and then to a create new album page,
this then creates a new album and returns to the home page
"""

def test_create_album_within_artist_page_return_home(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-artists")

    page.click("a:has-text('Pixies')")

    page.click("a:has-text('Create new album by Pixies')")

    page.fill("input[name='title']", "Bossanova")
    page.fill("input[name='release_year']", str(1990))
    
    page.click("input:has-text('Create Album')")
    page.screenshot(path="screenshot.png", full_page = True)
    strong_tags = page.locator("strong")
    
    expected_titles = [
        "Doolittle",
        "Surfer Rosa",
        "Bossanova"
    ]
    for index, title in enumerate(expected_titles):
        expect(strong_tags.nth(index)).to_have_text(title)


"""
We navigate from the artists page to a create artist page and then 
create a new artist then returning to the artists page
"""

def test_create_artist_within_artist_page_return_home(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-artists")

    page.click("a:has-text('Create new artist')")

    page.fill("input[name='name']", "Vince Staples")
    page.fill("input[name='genre']", "Rap")

    page.click("input:has-text('Create Artist')")

    div_tags = page.locator("div")
    
    expected_names = [
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone",
        "Vince Staples"
    ]
    for index, name in enumerate(expected_names):
        expect(div_tags.nth(index)).to_have_text(name)


"""
We try and create an album with missing attributes and
are returned an error message in the page
"""

def test_no_artist_name_returns_error_message(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-artists")
    
    
    page.click("a:has-text('Create new Artist')")

    page.fill("input[name='name']", "Mick Jenkins")
    page.fill("input[name='genre']", "")

    page.click("input:has-text('Create Artist')")
    page.screenshot(path="screenshot.png", full_page = True)
    errors = page.locator(".t-errors")

    expect(errors).to_have_text("There were errors with your submission: Artist has no genre.")



def test_no_album_name_returns_error_message(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/get-artists")
    
    
    page.click("a:has-text('Pixies')")

    page.click("a:has-text('Create new album by Pixies')")

    page.fill("input[name='title']", "")
    page.fill("input[name='release_year']", "1991")

    page.click("input:has-text('Create Album')")
    page.screenshot(path="screenshot.png", full_page = True)
    errors = page.locator(".t-errors")

    expect(errors).to_have_text("There were errors with your submission: Album has no title.")
