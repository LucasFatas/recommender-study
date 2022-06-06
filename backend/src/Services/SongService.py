from src.Services.database_config import DatabaseException, open_connection
import mysql.connector
from src.Entities.Song import Song
from dotenv import load_dotenv
import os

load_dotenv()


# Method that stores the top songs of a user
# Parameters: a userId and a list of song objects with a name, spotify_url and list of artist(s)
# Returns: a confirmation message
def add_top_songs(userId, songs, db, cursor, database):
    try:
        song_sql = "INSERT INTO " + database + ".Song(previewUrl, userId, name, spotifyUrl) VALUES (%s, %s, %s, %s)"
        artist_sql = "INSERT INTO " + database + ".Artist(spotifyUrl, name)  VALUES (%s, %s)"
        for song in songs:
            val = (song.preview_url, userId, song.name, song.spotify_url)
            cursor.execute(song_sql, val)
            for artist in song.artists:
                val = (song.spotify_url, artist['artist_name'])
                cursor.execute(artist_sql, val)
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing of top songs"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding songs.")


# Method that retrieves top songs of a user
# Parameter: a userId
# Returns: a list of song objects
def get_top_songs(userId, db, cursor, database):
    try:
        song_sql = "SELECT name, previewUrl, spotifyUrl FROM " + database + ".Song WHERE userId = %s"

        cursor.execute(song_sql, (userId,))

        data = cursor.fetchall()

        songs = []

        for row in data:
            artist_sql = "SELECT DISTINCT name FROM " + database + ".Artist Where spotifyUrl = %(url)s"

            cursor.execute(artist_sql, {'url': str(row[1])})

            artists = []

            for artist in cursor.fetchall():
                artists.append(artist[0])

            songs.append(Song(row[1], row[0], artists, row[2]))

        return songs
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when getting songs.")


# Method that stores the recommendation ratings of a user
# Parameters: a userId and a playlistRating, with userId, matchedUserId and rating.
# Returns: a confirmation message
def add_playlist_ratings(playlist, db, cursor, database):
    try:
        playlist_sql = "INSERT INTO " + database + ".PlaylistRating(userId, matchedUserId, rating) VALUES (%s, %s, %s)"

        val = (playlist.userId, playlist.matchedUserId, playlist.rating)
        cursor.execute(playlist_sql, val)

        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing playlist ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when storing playlist ratings.")


# Method that stores the recommendation ratings of a user
# Parameters: a userId and a list of song objects with a name, spotify_url and list of artist(s)
# Returns: a confirmation message
def add_song_ratings(song_ratings, db, cursor, database):

    """
    This method has been updated in branch 7/8-Retrieve-Batch-1/2-Data so don't create a test for this just yet.
    """
    try:
        song_sql = "Insert into " + database + ".SongRating(userId, matchedUserId, spotifyUrl, rating) Values (%s," \
                                               "%s,%s,%s) "
        for song_rating in song_ratings:
            val = (song_rating.userId, song_rating.matchedUserId, song_rating.spotify_url, song_rating.rating)
            cursor.execute(song_sql, val)

        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing song ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when storing song ratings.")



