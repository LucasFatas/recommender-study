from src.service import add_answers, open_connection

def test_add_answers():
    tup = [(1,1,1),(1,2,3)]
    assert "Success storing all Answers" == add_answers(tup)
