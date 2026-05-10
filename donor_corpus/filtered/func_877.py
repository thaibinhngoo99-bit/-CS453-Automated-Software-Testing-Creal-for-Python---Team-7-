def test_doit():
    from sympy import Symbol
    p = Symbol('p', positive=True)
    n = Symbol('n', negative=True)
    np = Symbol('np', nonpositive=True)
    nn = Symbol('nn', nonnegative=True)
    assert Gt(p, 0).doit() is S.true
    assert Gt(p, 1).doit() == Gt(p, 1)
    assert Ge(p, 0).doit() is S.true
    assert Le(p, 0).doit() is S.false
    assert Lt(n, 0).doit() is S.true
    assert Le(np, 0).doit() is S.true
    assert Gt(nn, 0).doit() == Gt(nn, 0)
    assert Lt(nn, 0).doit() is S.false
    assert Eq(x, 0).doit() == Eq(x, 0)