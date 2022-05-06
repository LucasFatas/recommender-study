from flask import Flask
import json


def create_app():
    app = Flask(__name__)

    with open('../config.json', 'r') as f:
        config = json.load(f)

    app.run(port=config['port'])

    return app


if __name__ == "__main__":
    create_app()
