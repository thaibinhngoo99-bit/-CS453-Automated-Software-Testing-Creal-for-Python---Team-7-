def test_bug2():
    e = x - y
    a = str(e)
    b = str(e)
    assert a == b