import mysql.connector
import json


# Exception if we can not reach the DataBase
class DatabaseException(Exception):
    pass


# Method that opens the connection to the database
def open_connection():

    db = mysql.connector.connect(
        # Change once it is no longer hosted
        host="localhost",
        user="temp_user",
        passwd="password",
        database="recommender"
    )

    cursor = db.cursor()

    return db, cursor, "recommender"
