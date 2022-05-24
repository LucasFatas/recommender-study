import json

from flask import Flask
from flask_cors import CORS

from src.Controllers.DashboardController import dashboard
from src.Controllers.QuestionnaireController import questionnaire
from src.Controllers.SongController import songs

app = Flask(__name__)
app.register_blueprint(songs, url_prefix='/spotify')
app.register_blueprint(questionnaire, url_prefix='/questionnaire')
app.register_blueprint(dashboard, url_prefix='/dashboard')


CORS(app)


def create_app():
    with open('config.json', 'r') as f:
        config = json.load(f)
    app.run(debug=True, port=config['port'])


if __name__ == "__main__":
    create_app()

