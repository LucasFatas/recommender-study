import mysql.connector
import os
from dotenv import load_dotenv


# Exception if we can not reach the DataBase
class DatabaseException(Exception):
    pass


# Method that opens the connection to the database
def open_connection():
    load_dotenv()
    db = mysql.connector.connect(
        # Change once it is no longer hosted
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )

    cursor = db.cursor()

    return db, cursor, "recommender"
