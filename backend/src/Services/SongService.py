from src.Services.database_config import DatabaseException, open_connection
import mysql.connector
from src.Entities.Song import Song
from dotenv import load_dotenv
import os

load_dotenv()


def add_top_songs(user_id, songs, db, cursor, database):
    """
    Stores top songs of a given user
    :param user_id: id of the participant
    :param songs: list of song objects symbolizing the song information
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: success message
    """
    try:
        song_sql = """
            INSERT INTO """ + database + """.Song(previewUrl, userId, name, spotifyUrl) VALUES (%s, %s, %s, %s)
        """
        artist_sql = """INSERT INTO """ + database + """.Artist(spotifyUrl, name) VALUES (%s, %s)"""

        for song in songs:
            val = (song.preview_url, user_id, song.name, song.spotify_url)
            cursor.execute(song_sql, val)
            for artist in song.artists:
                val = (song.spotify_url, artist['artist_name'])
                cursor.execute(artist_sql, val)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing of top songs"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when adding songs.")


def get_top_songs(userId, db, cursor, database):
    """
    Returns top songs of a user
    :param userId: id of the participant
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: a tuple with userId and their 5 top songs
    """
    try:
        sql = """SELECT name, previewUrl, spotifyUrl FROM """ + database + """.song WHERE userId = %s"""

        cursor.execute(sql, (userId,))

        data = cursor.fetchall()

        songs = []

        for row in data:
            artist_sql = "SELECT DISTINCT name FROM " + database + ".Artist Where spotifyUrl = %(url)s"

            cursor.execute(artist_sql, {'url': str(row[2])})

            artists = []

            for artist in cursor.fetchall():
                artists.append(artist[0])

            songs.append(Song(row[1], row[0], artists, row[2]))

        return songs
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when getting songs.")


def add_playlist_ratings(playlist, db, cursor, database):
    """
    Stores top songs of a given user
    :param playlist: playlist object with userId, matchedUserId and rating of the playlist
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: result with all the users of a provided batch along with their answers to the questionnaires
    """
    try:
        sql = """
            INSERT INTO """ + database + """.PlaylistRating(userId, matchedUserId, rating) 
            VALUES (%s, %s, %s)
        """

        val = (playlist.userId, playlist.matchedUserId, playlist.rating)
        cursor.execute(sql, val)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing playlist ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when storing playlist ratings.")


def add_song_ratings(song_ratings, db, cursor, database):
    """
    Stores all the song ratings into the database, along with an index to keep track of the order of the playlist
    :param song_ratings: the ratings of the songs, provided in a list of SongRatings
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :raises DatabaseException: custom exception in our app, in order for better handling when database commands fail
    :return: Success message
    """
    try:
        sql = """
            INSERT INTO """ + database + """.SongRating(userId, matchedUserId, spotifyUrl, 
            rating, playlistNumber)
            VALUES (%s,%s,%s,%s,%s) 
        """
        for song_rating in song_ratings:
            val = (song_rating.userId, song_rating.matchedUserId, song_rating.spotify_url,
                   song_rating.rating, song_rating.playlistNumber)
            cursor.execute(sql, val)

        # Commit only if we are not testing the application
        if os.getenv('IS_TESTING') == "FALSE":
            db.commit()
        return "Success storing song ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        db.rollback()
        raise DatabaseException("Error connecting to database when storing song ratings.")
