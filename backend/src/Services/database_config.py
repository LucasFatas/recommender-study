import mysql.connector
import os
from dotenv import load_dotenv


class DatabaseException(Exception):
    """
    Handles database connection errors in our app.
    """
    pass


def open_connection():
    """
    Method that opens the connection to the database, depends on the .env file.
    :return: a triplet with the database connection object, the cursor for the SQL commands, and the database name.
    """
    load_dotenv()
    # Case for when we are in testing mode for the database.
    if os.getenv('IS_TESTING') == "TRUE":
        database = os.getenv('DB_TEST_DATABASE')
    # Case for when the app is deployed, and we are not testing anymore.
    else:
        database = os.getenv('DB_DATABASE')
    db = mysql.connector.connect(
        # Change once it is no longer hosted locally
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        database=database
    )

    cursor = db.cursor()

    return db, cursor, database
