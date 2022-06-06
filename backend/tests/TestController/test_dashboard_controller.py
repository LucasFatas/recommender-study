from src.main import app


def test_retrieve_scores(set_up):

    response = app.test_client().get("/dashboard/scores?batchId=1")



