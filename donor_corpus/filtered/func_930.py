def test_Limit():
    assert str(Limit(sin(x) / x, x, y)) == 'Limit(sin(x)/x, x, y)'
    assert str(Limit(1 / x, x, 0)) == 'Limit(1/x, x, 0)'
    assert str(Limit(sin(x) / x, x, y, dir='-')) == "Limit(sin(x)/x, x, y, dir='-')"