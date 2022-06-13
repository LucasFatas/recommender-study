import json

from flask import Flask
from flask_cors import CORS

from src.Controllers.Dashboard.DashboardCSVController import CSVDashboard
from src.Controllers.Dashboard.DashboardLoginController import loginDashboard
from src.Controllers.Dashboard.DashboardParametersController import parameterDashboard

from src.Controllers.QuestionnaireController import questionnaire
from src.Controllers.SongController import songs
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(songs, url_prefix='/spotify')
app.register_blueprint(questionnaire, url_prefix='/questionnaire')
app.register_blueprint(CSVDashboard, url_prefix='/dashboard/csv')
app.register_blueprint(loginDashboard, url_prefix='/dashboard/login')
app.register_blueprint(parameterDashboard, url_prefix='/dashboard/parameters')


CORS(app, resources={r"/*": {"origins": "*"}})
load_dotenv()


def create_app():
    app.run(debug=True, port=os.getenv('PORT'))


if __name__ == "__main__":
    os.environ['IS_TESTING'] = 'FALSE'
    create_app()

