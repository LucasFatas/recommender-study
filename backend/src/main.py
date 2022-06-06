import json

from flask import Flask
from flask_cors import CORS

from src.Controllers.DashboardController import dashboard
from src.Controllers.QuestionnaireController import questionnaire
from src.Controllers.SongController import songs
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(songs, url_prefix='/spotify')
app.register_blueprint(questionnaire, url_prefix='/questionnaire')
app.register_blueprint(dashboard, url_prefix='/dashboard')


CORS(app, resources={r"/*": {"origins": "*"}})
load_dotenv()


def create_app():

    app.run(debug=True, port=os.getenv('PORT'))


if __name__ == "__main__":
    os.environ['IS_TESTING'] = 'FALSE'
    create_app()

