def test_canonical():
    one = S(1)

    def unchanged(v):
        c = v.canonical
        return v.is_Relational and c.is_Relational and (v == c)

    def isreversed(v):
        return v.canonical == v.reversed
    assert unchanged(x < one)
    assert unchanged(x <= one)
    assert isreversed(Eq(one, x, evaluate=False))
    assert unchanged(Eq(x, one, evaluate=False))
    assert isreversed(Ne(one, x, evaluate=False))
    assert unchanged(Ne(x, one, evaluate=False))
    assert unchanged(x >= one)
    assert unchanged(x > one)
    assert unchanged(x < y)
    assert unchanged(x <= y)
    assert isreversed(Eq(y, x, evaluate=False))
    assert unchanged(Eq(x, y, evaluate=False))
    assert isreversed(Ne(y, x, evaluate=False))
    assert unchanged(Ne(x, y, evaluate=False))
    assert isreversed(x >= y)
    assert isreversed(x > y)
    assert (-x < 1).canonical == (x > -1)
    assert isreversed(-x > y)