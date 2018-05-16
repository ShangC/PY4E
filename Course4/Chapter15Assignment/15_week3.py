import xml.etree.ElementTree as ET
import sqlite3
import os

conn = sqlite3.connect("C15W3DB.sqlite")
cur = conn.cursor()

cur.executescript(
    '''DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        );

    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
        );

    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, 
        rating INTEGER,
        count INTEGER
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
''')

print("1 -- Windows VS Code")
print("2 -- Local Terminal")

RunEnvir = input("Choose Python execution environment:")
if RunEnvir == "1":
    XmlName = os.path.join(os.path.dirname(__file__), "library.xml")
if RunEnvir == "2":
    XmlName = "library.xml"

   
    
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == "key" and child.text == key :
            found = True
    return None

XmlData = ET.parse(XmlName)
TrackData = XmlData.findall("dict/dict/dict")
print("Track Count:", len(TrackData))

artistList = []
albumList = []
genreList = []

for track in TrackData:
    if (lookup(track, "Track ID") is None):
        continue
    name = lookup(track, "Name")
    artist = lookup(track, "Artist")
    album = lookup(track, "Album")
    count = lookup(track, "Play Count")
    rating = lookup(track, "Rating")
    length = lookup(track, "Total Time")
    genre = lookup(track, "Genre")

    artistList.append(artist)
    albumList.append(album)
    genreList.append(genre)
    
    if name is None or artist is None or album is None or genre is None:
        continue
    
    print(name, artist, album, genre, count, rating, length)
       
    # if artist in artistList:
    #     continue
    cur.execute(
        '''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist,)
    )
    cur.execute(
        '''SELECT id FROM Artist 
        WHERE name = ?''', (artist,)
    )
    artist_id = cur.fetchone()[0]

    # if album in albumList:
    #     continue
    cur.execute(
        '''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id)
    )
    cur.execute(
        '''SELECT id FROM Album
        WHERE title = ?''', (album,)
    )
    album_id = cur.fetchone()[0]

    # if genre in genreList:
    #     continue
    cur.execute(
        '''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre,)
    )
    cur.execute(
        '''SELECT id FROM Genre 
        WHERE name = ?''', (genre,)
    )
    genre_id = cur.fetchone()[0]
    # print(genre_id)

    cur.execute(
        '''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, genre_id, length, rating, count) 
    )

    conn.commit()

