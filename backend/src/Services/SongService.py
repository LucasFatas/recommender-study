from src.Services.database_config import DatabaseException, open_connection
import mysql.connector
from src.Entities.Song import Song
from src.Entities.SongRating import SongRating


# Method that stores the top songs of a user
# Parameters: a userId and a list of song objects with a name, spotify_url and list of artist(s)
# Returns: a confirmation message
def add_top_songs(userId, songs):
    try:
        db, cursor, database = open_connection()
        song_sql = "Insert into " + database + ".song(preview_url, userId, name, spotify_url) Values (%s, %s, %s, %s)"
        artist_sql = "Insert into recommender.Artist(spotify_url, name)  Values(%s, %s)"
        for song in songs:
            val = (song.preview_url, userId, song.name, song.spotify_url)
            cursor.execute(song_sql, val)
            for artist in song.artists:
                val = (song.spotify_url, artist['artist_name'])
                cursor.execute(artist_sql, val)
        db.commit()
        return "Success storing of top songs"
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when adding songs.")


# Method that retrieves top songs of a user
# Parameter: a userId
# Returns: a list of song objects
def get_top_songs(userId):
    try:
        db, cursor, database = open_connection()
        song_sql = "Select name, preview_url, spotify_url from " + database + ".song Where userId = " + str(userId)

        cursor.execute(song_sql)

        data = cursor.fetchall()

        songs = []

        for row in data:
            artist_sql = "Select distinct name from " + database + ".Artist Where spotify_url = %(url)s"

            cursor.execute(artist_sql, {'url': str(row[1])})

            artists = []

            for artist in cursor.fetchall():
                artists.append(artist[0])

            songs.append(Song(row[1], row[0], artists, row[2]))

        return songs
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when getting songs.")


# Method that stores the recommendation ratings of a user
# Parameters: a userId and a list of three playlistRatings, each with userId, matchedUserId and rating.
# Returns: a confirmation message
def add_playlist_ratings(playlist):
    try:
        db, cursor, database = open_connection()
        playlist_sql = "Insert into " + database + ".PlaylistRating(userId, matchedUserId, rating) Values (%s, %s, %s)"

        val = (playlist.userId, playlist.matchedUserId, playlist.rating)
        cursor.execute(playlist_sql, val)

        db.commit()
        return "Success storing playlist ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when storing playlist ratings.")


# Method that stores the recommendation ratings of a user
# Parameters: a userId and a list of song objects with a name, spotify_url and list of artist(s)
# Returns: a confirmation message
def add_song_ratings(song_ratings):
    try:
        db, cursor, database = open_connection()
        song_sql = "Insert into " + database + ".SongRating(userId, matchedUserId, spotify_url, rating, playlistNumber) " \
                                               "Values (%s,%s,%s,%s,%s) "
        for song_rating in song_ratings:
            val = (song_rating.userId, song_rating.matchedUserId, song_rating.spotify_url,
                   song_rating.rating, song_rating.playlistNumber)
            cursor.execute(song_sql, val)

        db.commit()
        return "Success storing song ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when storing song ratings.")
