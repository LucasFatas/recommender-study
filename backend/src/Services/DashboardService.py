import mysql.connector
from src.Services.database_config import DatabaseException, open_connection


# Method that gets all the users of a certain batch and their questionnaire scores
# Parameters: batch number
# Returns: a list of tuples containing userId and their scores
def get_all_scores(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select UserID, Openness, Honesty, Emotionality, Extroversion, Agreeableness, Conscientiousness," \
            " Stimulation, SelfDirection, Universalism, Benevolence, Tradition, Conformity, SecurityVal, PowerVal, " \
            "Achievement, Hedonism "\
            "From recommender.personality as pe Inner Join recommender.participant as pa on pe.PersonalityId = "\
            "pa.UserId Inner Join recommender.value as v on v.ValueId = pa.UserId Where pa.Batch = %s"

        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


# Method that gets all the answers of users of a certain batch
# Parameters: batch number
# Returns: a list of tuples containing userId, question number, answer
def get_all_answers(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select p.UserId, QuestionNumber, Response from recommender.Answer as a Left Join recommender.participant" \
              " as p on a.UserId=p.UserId Where p.Batch = %s"
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


# Method that gets all the songs of users of a certain batch
# Parameters: batch number
# Returns: a list of tuples containing userId, spotify_url
def get_all_songs(batch):
    try:
        db, cursor, database = open_connection()
        sql = "Select p.UserId, spotify_url from recommender.song as s Left Join recommender.participant" \
              " as p on s.UserId=p.UserId Where p.Batch = %s"
        cursor.execute(sql, (batch,))
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Scores.")


# Method that gets all the feedback (except individual songs) of users.
# Returns: a list of tuples containing userId and for each match, the id of the matched user, the rating of the match
# and the answer to each question about the match answered by the user.
def get_all_match_data():
    try:
        db, cursor, database = open_connection()

        # Calculate the amount of questions being asked in this instance of the experiment.
        sql_questions = "select count(distinct(questionNumber)) from recommender.questionfeedback"
        cursor.execute(sql_questions)
        number_of_questions = cursor.fetchall()[0][0]

        # Retrieve all data from the database based on the matches made by our app. We use three different temporary
        # tables with the feedback from each match and then join them.
        sql = """
        with table1 as (
            Select m.userId, m.valueId, pr1.rating, group_concat(qf1.answer order by qf1.questionNumber), of1.feedback
            from recommender.matches as m 
            join recommender.PlaylistRating as pr1 on pr1.userId = m.userId and pr1.matchedUserId = m.ValueId
            join recommender.QuestionFeedback as qf1 on qf1.userId = m.userId and qf1.matchedUserId = m.ValueId
            join recommender.OpenFeedback as of1 on of1.userId = m.userId and of1.matchedUserId = m.ValueId)
        , table2 as (
            Select m.userId, m.personalityId, pr2.rating, group_concat(qf2.answer order by qf2.questionNumber), of2.feedback
            from recommender.matches as m 
            join recommender.PlaylistRating as pr2 on pr2.userId = m.userId and pr2.matchedUserId = m.personalityId 
            join recommender.QuestionFeedback as qf2 on qf2.userId = m.userId and qf2.matchedUserId = m.personalityId 
            join recommender.OpenFeedback as of2 on of2.userId = m.userId and of2.matchedUserId = m.personalityId)
        , table3 as (
            Select m.userId, m.randomId, pr3.rating, group_concat(qf3.answer order by qf3.questionNumber), of3.feedback 
            from recommender.matches as m 
            join recommender.PlaylistRating as pr3 on pr3.userId = m.userId and pr3.matchedUserId = m.randomId 
            join recommender.QuestionFeedback as qf3 on qf3.userId = m.userId and qf3.matchedUserId = m.randomId 
            join recommender.OpenFeedback as of3 on of3.userId = m.userId and of3.matchedUserId = m.randomId)
            
        select * from table1 
            join table2 on table1.userId = table2.userId
            join table3 on table1.userId = table3.userId
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        return result, number_of_questions

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving match feedback")


# Method that gets all the song ratings of users of batch 2
# Returns: list of tuples containing userId and for each match and the rating of each song recommendation (0 if empty).
def get_song_ratings():
    try:
        db, cursor, database = open_connection()

        # Retrieve all data from the database based on the matches made by our app.
        sql = """
        with 
        table1 as (
                    Select m.userId, group_concat(sr1.playlistNumber, '-', sr1.rating order by sr1.playlistNumber) as answers
                    from recommender.matches as m 
                    join recommender.songRating as sr1 on m.userId = sr1.userId and m.valueId = sr1.matchedUserId)
        , table2 as (
                    Select m.userId, group_concat(sr2.playlistNumber, '-', sr2.rating order by sr2.playlistNumber) as answers
                    from recommender.songRating as sr2 
                    join recommender.matches as m on m.userId = sr2.userId and m.personalityId = sr2.matchedUserId)
        , table3 as (
                    Select m.userId, group_concat(sr3.playlistNumber, '-', sr3.rating order by sr3.playlistNumber) as answers
                    from recommender.songRating as sr3 
                    join recommender.matches as m on m.userId = sr3.userId and m.randomId = sr3.matchedUserId)
        
        select table1.userId, table1.answers, table2.answers, table3.answers from table1 
            join table2 on table1.userId = table2.userId
            join table3 on table1.userId = table3.userId;
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except mysql.connector.errors.Error as e:
        print(e)
        raise DatabaseException("Error connecting to database when retrieving Song ratings.")
