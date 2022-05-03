import pytest
from src.main import create_app
import json


@pytest.fixture()
def app():
    with open('../config.json', 'r') as f:
        configuration = json.load(f)

    configuration['is_testing']

    with open("../config.json", "w") as f:
        json.dump(configuration, f)

    app = create_app()

    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
