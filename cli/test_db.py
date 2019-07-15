import db_cla

def test_set():
    result = db_cla.set_req(['name', 'hello'])

    assert result == 'OK'

def test_get():
    db_cla.set_req(['hello', 'world'])

    result = db_cla.get_req(['name'])

    assert result == 'hello'

def test_del():
    db_cla.set_req(['python', 'code'])

    result1 = db_cla.del_req(['python'])
    result2 = db_cla.get_req(['python'])

    assert result1 == 'OK' and result2 == 'None'

def test_incr():
    db_cla.set_req(['cnt', '100'])

    result = db_cla.incr_req(['cnt'])

    assert result == '101.0'
    print(11)
