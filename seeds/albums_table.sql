DROP TABLE IF EXISTS albums CASCADE;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

DROP TABLE IF EXISTS artists CASCADE;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');

INSERT INTO albums (title, release_year, artist_id) VALUES('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES('Surfer Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES('Waterloo', 1974, 2);
