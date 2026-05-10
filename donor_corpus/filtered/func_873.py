def test_Eq():
    assert Eq(x ** 2) == Eq(x ** 2, 0)
    assert Eq(x ** 2) != Eq(x ** 2, 1)
    assert Eq(x, x)
    p = Symbol('p', positive=True)
    assert Eq(p, 0) is S.false