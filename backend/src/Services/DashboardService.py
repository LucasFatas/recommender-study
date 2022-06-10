import mysql.connector
from src.Services.database_config import DatabaseException
from dotenv import load_dotenv

load_dotenv()


def get_all_scores(batch, db, cursor, database):
    """
    Retrieves all the personality and value scores of all users in a specific batch from the database
    :param batch: batch to get the information about
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: result with all the users of a provided batch along with their scores
    """
    try:
        sql = """ 
            SELECT pa.userId, honesty, emotionality, extroversion, agreeableness, conscientiousness, openness,
            stimulation, selfDirection, universalism, benevolence, tradition, conformity, securityVal, powerVal,
            achievement, hedonism 
            FROM """ + database + """.Personality AS pe 
            INNER JOIN """ + database + """.Participant AS pa ON pe.userId = pa.userId 
            INNER JOIN """ + database + """.Value AS v ON v.userId = pa.userId 
            WHERE pa.batch = %s 
        """

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


def get_all_answers(batch, db, cursor, database):
    """
    Retrieves all the answers to the questionnaire questions of all users in a specific batch from the database
    :param batch: batch to get the information about
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: result with all the users of a provided batch along with their answers to the questionnaires
    """
    try:
        sql = """
            SELECT p.userId, questionNumber, response FROM """ + database + """.Answer AS a 
            LEFT JOIN """ + database + """.Participant AS p ON a.userId = p.userId 
            WHERE p.batch = %s
        """
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


def get_all_songs(batch, db, cursor, database):
    """
    Retrieves all the songs of all users in a specific batch from the database
    :param batch: batch to get the information about
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: result with all the users of a provided batch along with their scores
    """
    try:
        sql = """
            SELECT p.userId, spotifyUrl FROM """ + database + """.Song AS s 
            LEFT JOIN """ + database + """.Participant AS p ON s.userId = p.userId 
            WHERE p.batch = %s
        """
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


def get_all_match_data(db, cursor, database):
    """
    Retrieves all the match information of all users from the database
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: result with all the users from batch 2 along with their matches
    and the feedback provided to the playlist of each match
    """
    try:
        # Calculate the amount of questions being asked in this instance of the experiment.
        sql_questions = "SELECT COUNT(DISTINCT(questionNumber)) FROM " + database + ".QuestionFeedback"
        cursor.execute(sql_questions)
        number_of_questions = cursor.fetchall()[0][0]

        # Retrieve all data from the database based on the matches made by our app. We use three different temporary
        # tables with the feedback from each match and then join them.
        sql = """
            WITH 
                table1 AS (
                    SELECT m.userId, m.valueId, pr1.rating, 
                        GROUP_CONCAT(qf1.answer ORDER BY qf1.questionNumber), of1.feedback
                    FROM """ + database + """.Matches AS m 
                    JOIN """ + database + """.PlaylistRating AS pr1 
                        ON pr1.userId = m.userId AND pr1.matchedUserId = m.ValueId
                    JOIN """ + database + """.QuestionFeedback AS qf1 
                        ON qf1.userId = m.userId AND qf1.matchedUserId = m.ValueId
                    LEFT JOIN """ + database + """.OpenFeedback AS of1 
                        ON of1.userId = m.userId AND of1.matchedUserId = m.ValueId
                    GROUP BY m.userId, m.valueId
                )
            
                , table2 AS (
                    SELECT m.userId, m.personalityId, pr2.rating, 
                        GROUP_CONCAT(qf2.answer ORDER BY qf2.questionNumber), of2.feedback
                    FROM """ + database + """.Matches AS m 
                    JOIN """ + database + """.PlaylistRating AS pr2 
                        ON pr2.userId = m.userId AND pr2.matchedUserId = m.personalityId 
                    JOIN """ + database + """.QuestionFeedback AS qf2 
                        ON qf2.userId = m.userId AND qf2.matchedUserId = m.personalityId 
                    LEFT JOIN """ + database + """.OpenFeedback AS of2 
                        ON of2.userId = m.userId AND of2.matchedUserId = m.personalityId
                    GROUP BY m.userId, m.personalityId
                )
            
                , table3 AS (
                    SELECT m.userId, m.randomId, pr3.rating, 
                        GROUP_CONCAT(qf3.answer ORDER BY qf3.questionNumber), of3.feedback 
                    FROM """ + database + """.Matches AS m 
                    JOIN """ + database + """.PlaylistRating AS pr3 
                        ON pr3.userId = m.userId AND pr3.matchedUserId = m.randomId 
                    JOIN """ + database + """.QuestionFeedback AS qf3 
                        ON qf3.userId = m.userId AND qf3.matchedUserId = m.randomId 
                    LEFT JOIN """ + database + """.OpenFeedback AS of3 
                        ON of3.userId = m.userId AND of3.matchedUserId = m.randomId
                    GROUP BY m.userId, m.randomId    
                )
                
            SELECT * FROM table1 
            JOIN table2 ON table1.userId = table2.userId
            JOIN table3 ON table1.userId = table3.userId
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        return result, number_of_questions

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving match feedback")


def get_song_ratings(db, cursor, database):
    """
    Retrieves all the song ratings of all users from the database
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: result with all the users of batch 2 along with their song ratings (only the non-zero ones)
    """
    try:
        # Retrieve all data from the database based on the matches made by our app.
        sql = """
            WITH 
                table1 AS (
                    SELECT m.userId, GROUP_CONCAT(sr1.playlistNumber, '-', sr1.rating ORDER BY sr1.playlistNumber) 
                    AS answers
                    FROM """ + database + """.Matches AS m 
                    LEFT JOIN """ + database + """.songRating AS sr1 
                        ON m.userId = sr1.userId AND m.valueId = sr1.matchedUserId
                    GROUP BY m.userId
                )
                
                , table2 AS (
                    SELECT m.userId, GROUP_CONCAT(sr2.playlistNumber, '-', sr2.rating ORDER BY sr2.playlistNumber) 
                    AS answers
                    FROM """ + database + """.songRating AS sr2 
                    LEFT JOIN """ + database + """.Matches AS m 
                        ON m.userId = sr2.userId AND m.personalityId = sr2.matchedUserId 		
                    GROUP BY m.userId
                )
                    
                , table3 AS (
                    SELECT m.userId, GROUP_CONCAT(sr3.playlistNumber, '-', sr3.rating ORDER BY sr3.playlistNumber) 
                    AS answers
                    FROM """ + database + """.songRating AS sr3 
                    LEFT JOIN """ + database + """.Matches AS m 
                        ON m.userId = sr3.userId AND m.randomId = sr3.matchedUserId
                    GROUP BY m.userId
                )
            
            SELECT table1.userId, table1.answers, table2.answers, table3.answers FROM table1 
            LEFT JOIN table2 ON table1.userId = table2.userId
            LEFT JOIN table3 ON table1.userId = table3.userId;
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Song ratings.")


def get_user_total(batch, db, cursor, database):
    """
    Retrieves the total number of users that have completed the questionnaire
    :param batch: batch to get the information about
    :param db: database object, handles the connection to our database
    :param cursor: cursor that executes the SQL commands in our database
    :param database: string of the database name we will be using
    :except mysql.connector.errors.Error: handles the case where the database has some errors
    :raises DatabaseException: custom exception in our app, in order for better handling
    :return: total number of users
    """
    try:
        sql = """
            SELECT COUNT(DISTINCT(Participant.userId)) FROM """ + database + """.Participant 
            INNER JOIN """ + database + """.Personality AS p ON p.userId = Participant.userId
            INNER JOIN """ + database + """.Value AS v ON v.userId = Participant.userId
            WHERE batch = %s
        """

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()

        return str(result[0][0])
    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Song ratings.")
