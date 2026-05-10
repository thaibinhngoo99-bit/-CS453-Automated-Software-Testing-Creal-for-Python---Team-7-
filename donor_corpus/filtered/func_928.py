def test_Integer():
    assert str(Integer(-1)) == '-1'
    assert str(Integer(1)) == '1'
    assert str(Integer(-3)) == '-3'
    assert str(Integer(0)) == '0'
    assert str(Integer(25)) == '25'