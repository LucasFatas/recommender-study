import json

from flask import Flask
from flask_cors import CORS
from werkzeug.utils import import_string

from src.Controllers.QuestionnaireController import questionnaire
from src.Controllers.SongController import songs
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(songs, url_prefix='/spotify')
app.register_blueprint(questionnaire, url_prefix='/questionnaire')

CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()


def create_app():
    api_blueprints = [
        'DashboardLoginController',
        'DashboardCSVController',
        'DashboardParametersController'
    ]

    for bp_name in api_blueprints:
        blueprint = import_string('src.Controllers.Dashboard.%s:dashboard' % bp_name)
        app.register_blueprint(blueprint, name=bp_name)

    app.run(debug=True, port=os.getenv('PORT'))


if __name__ == "__main__":
    os.environ['IS_TESTING'] = 'FALSE'
    create_app()

