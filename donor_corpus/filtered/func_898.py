def test_reversed():
    assert (x < y).reversed == (y > x)
    assert (x <= y).reversed == (y >= x)
    assert Eq(x, y, evaluate=False).reversed == Eq(y, x, evaluate=False)
    assert Ne(x, y, evaluate=False).reversed == Ne(y, x, evaluate=False)
    assert (x >= y).reversed == (y <= x)
    assert (x > y).reversed == (y < x)