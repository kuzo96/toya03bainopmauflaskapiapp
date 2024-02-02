from src.app import app


class Test:

  def test(self):
    c = app.test_client()  # get test client of flask app  ref https://stackoverflow.com/a/65883349/248616
    r = c.get('/')
    assert r.status_code == 200
    assert r.json == {}
