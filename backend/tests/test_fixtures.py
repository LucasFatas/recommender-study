import os

import pytest
from dotenv import load_dotenv
from src.Services.database_config import open_connection


@pytest.fixture(scope='function')
def set_up():
    load_dotenv()
    os.environ['IS_TESTING'] = 'TRUE'
    db, cursor, database = open_connection()

    yield db, cursor, database

    os.environ['IS_TESTING'] = 'FALSE'
    db.close()