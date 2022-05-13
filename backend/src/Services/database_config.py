import mysql.connector
import json


# Exception if we can not reach the DataBase
class DatabaseException(Exception):
    pass


def change_database_for_testing(value):
    with open('../config.json', 'r+') as f:
        data = json.load(f)
        data['is_testing'] = json.dumps(value)

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


# Method that opens the connection to the database
def open_connection():

    db = mysql.connector.connect(
        # Change once it is no longer hosted
        host="localhost",
        user="root",
        passwd="password",
        database="recommender"
    )

    cursor = db.cursor()

    return db, cursor,"recommender"
