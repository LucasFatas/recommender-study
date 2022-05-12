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
    with open('config.json', 'r') as f:
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
