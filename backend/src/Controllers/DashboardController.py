from flask import request, Blueprint, jsonify

from src.Services.DashboardService import get_all_scores

dashboard = Blueprint('dashboard', __name__)


@dashboard.route("/scores")
def retrieve_scores():
    batchId = request.get_json(force=True)['batchId']

    scores = get_all_scores(batchId)

    print(scores)


