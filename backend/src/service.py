import mysql.connector
import json
from random import randrange
from src.Entities.Song import Song

#Exception if we can not reach the DataBase
class DatabaseException(Exception):
    pass


def change_database_for_testing(value):
    with open('../config.json', 'r+') as f:
        data = json.load(f)
        data['is_testing'] = json.dumps(value)

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

#Method that opens the connection to the database
def open_connection():

    with open('../config.json', 'r') as f:
        configuration = json.load(f)

    if configuration['is_testing']:
        database = configuration['test_database']
    else:
        database = configuration['database']

    db = mysql.connector.connect(
        # Change once it is no longer hosted
        host="localhost",
        user="root",
        passwd="password",
        database=database
    )

    cursor = db.cursor()

    return db, cursor, database


# Method that stores all answers of a user to the database
# Parameters: a list of tuples containing: a user id, the question number and the user's answer
# Returns: A confirmation message
def add_answers(answers):
    try:
        db, cursor, database = open_connection()
        # The SQL statement for storing answers in the Answer table
        sql = "INSERT INTO " + database + ".Answer(UserId, QuestionNumber, Response) VALUES (%s, %s, %s)"

        cursor.executemany(sql, answers)
        db.commit()
        return "Success storing all Answers"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding answers.")


# Method that stores a new user to the database
# Parameters: a batch id
# Returns: a user id
def add_user(batch_id):
    try:
        db, cursor, database = open_connection()
        cursor.execute("Insert Into " + database + ".Participant(Batch) Values (" + str(batch_id) + ")")

        participant_id = cursor.lastrowid

        db.commit()
        return participant_id

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding users.")


# Method that stores the value vector of a user to the database
# Parameters: a user id and a value vector
# Returns: A confirmation message
def add_value(user_id, values):
    try:
        # The SQL statement for storing a value in the Value table
        db, cursor, database = open_connection()
        sql = "INSERT INTO " + database + ".Value (ValueId, Stimulation, SelfDirection, Universalism" \
              ",Benevolence,Tradition, Conformity, SecurityVal, PowerVal, Achievement,Hedonism)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, values[0], values[1], values[2], values[3], values[4],
               values[5], values[6], values[7], values[8], values[9])
        cursor.execute(sql, val)
        db.commit()

        return "Success storing value"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding values.")


# Method that stores the personality vector of a user to the database
# Parameters: a user id and a personality vector
# Returns: A confirmation message
def add_personality(user_id, personality):
    try:
        # The SQL statement for storing a personality in the Personality table
        db, cursor, database = open_connection()
        sql = "INSERT INTO " + database + ".Personality (PersonalityId, Openness, Honesty, Emotionality" \
              ", Extroversion, Agreeableness, Conscientiousness) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (user_id, personality[0], personality[1], personality[2],
               personality[3], personality[4], personality[5])
        cursor.execute(sql, val)
        db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding personalities.")


# Method that stores a user and his matches on personality and value and a random other user
# Parameters: a user id , a value user id, a personality user id and a random user id
# Returns: A confirmation message
def add_matches(userId, val_user, pers_user, random_user):
    try:
        # The SQL statement for storing user id and matches in the Match table
        db, cursor = open_connection()
        sql = "INSERT INTO Recommender.Match (UserId, ValId, PersId, RandId) VALUES (%s, %s, %s, %s)"
        val = (userId, val_user, pers_user, random_user)
        cursor.execute(sql, val)
        db.commit()

        return "Success storing personality"

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when adding personalities.")


# Method that stores the top songs of a user
# Parameters: a userId and a list of song objects with a name, spotify_url and list of artist(s)
# Returns: a confirmation message
def add_top_songs(userId, songs):
    try:
        db, cursor = open_connection()
        song_sql = "Insert into Recommender.song(spotify_url, userId, name) Values (%s, %s, %s)"
        artist_sql = "Insert into recommender.Artist(spotify_url, name)  Values(%s, %s)"
        for song in songs:
            val = (song.spotify_url, userId, song.name)
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
        db, cursor = open_connection()
        song_sql = "Select name, spotify_url from Recommender.song Where userId=" + str(userId)

        cursor.execute(song_sql)

        data = cursor.fetchall()

        songs = []

        artist_sql = "Select distinct name from recommender.Artist Where spotify_url=%s"

        for row in data:
            cursor.execute(artist_sql, (row[1], ))

            artists = []

            for artist in cursor.fetchall():
                artists.append(artist[0])

            songs.append(Song(row[1], row[0], artists))

        return songs
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when getting songs.")


# Method that stores the recommendation ratings of a user
# Parameters: a userId and a list of three playlistRatings, each with userId, matchedUserId and rating.
# Returns: a confirmation message
def add_playlist_ratings(playlists):
    try:
        db, cursor = open_connection()
        playlist_sql = "Insert into Recommender.PlaylistRating(userId, matchedUserId, rating) Values (%s, %s, %s)"
        for playlist in playlists:
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
        db, cursor = open_connection()
        song_sql = "Insert into Recommender.SongRating(userId, matchedUserId, spotify_url, rating) Values (%s,%s,%s,%s)"
        for song_rating in song_ratings:
            val = (song_rating.userId, song_rating.matchedUserId, song_rating.spotify_url, song_rating.rating)
            cursor.execute(song_sql, val)

        db.commit()
        return "Success storing song ratings"
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when storing song ratings.")


# Method that gets all the users of a certain batch and their values
# Parameters: batch number
# Returns: a list of tuples containing user and his values
def get_all_values(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserId, Stimulation, SelfDirection, Universalism, Benevolence," \
              " Tradition, Conformity, SecurityVal, PowerVal, Achievement, Hedonism " \
              "From recommender.value as v , recommender.participant as p " \
              "Where v.ValueId = p.UserId and p.Batch = " + str(batch)

        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when retrieving values.")


# Method that gets all the users of a certain batch and their personalities
# Parameters: batch number
# Returns: a list of tuples containing user and his personalities
def get_all_personalities(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserID, Openness, Honesty, Emotionality," \
              "Extroversion, Agreeableness, Conscientiousness " \
              "From " + database + ".personality as pe , " \
              + database + ".participant as pa " \
              "Where pe.PersonalityId = pa.UserId and p.Batch = " + str(batch)

        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when retrieving personalities.")


# Method that gets all the users of a certain batch apart from the value user and personality user
# Parameters: batch number
# Returns: one random user id
def get_random_user(user1, user2, batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserID From " + database + ".participant as p " \
              "Where p.Batch = " + str(batch) +" and not (p.UserID =" + str(user1) + " or p.UserID =  " + str(user2) + ")"


        cursor.execute(sql)
        result = cursor.fetchall()

        return result[randrange(0, len(result))]
    except mysql.connector.errors.Error as e:
        raise DatabaseException("Error connecting to database when retrieving users.")



if __name__ == '__main__':
    change_database_for_testing(False)

    get_random_user(2,6,1)