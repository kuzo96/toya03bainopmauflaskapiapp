from src.app import app


class Test:

  def test2311070900__release(self):
    c = app.test_client()  # get test client of flask app  ref https://stackoverflow.com/a/65883349/248616
    r = c.get('/release')
    assert r.status_code == 200

    d = r.json
    assert isinstance(d, list)
    assert len(d)>0

    i = d[0]
    k='created_at' ; assert i.get(k)
    k='tag_name'   ; assert i.get(k)
    k='body'       ; assert i.get(k)

  def test2311070904__most_3_recent_release(self):
    c = app.test_client()  # get test client of flask app  ref https://stackoverflow.com/a/65883349/248616
    r = c.get('/most_3_recent/release')
    assert r.status_code == 200

    d = r.json
    assert isinstance(d, list)
    assert len(d)<=3

    i = d[0]
    k='created_at' ; assert i.get(k)
    k='tag_name'   ; assert i.get(k)
    k='body'       ; assert i.get(k)

    #region ensure @ most recent logic
    release_all      = c.get('/release').json
    created_at__list = [ i['created_at'] for i in release_all]
    created_at__list = sorted(created_at__list, reverse=True) [:3]

    EXP_created_at = created_at__list
    ACT_created_at = _ = [ i['created_at'] for i in d]   ; _=sorted(_, reverse=True) [:3]   ; ACT_created_at=_
    assert ACT_created_at == EXP_created_at, 'ERROR most recent logic is incorrect'
    #endregion ensure @ most recent logic
