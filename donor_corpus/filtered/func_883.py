def test_evaluate():
    assert str(Eq(x, x, evaluate=False)) == 'Eq(x, x)'
    assert Eq(x, x, evaluate=False).doit() == S.true
    assert str(Ne(x, x, evaluate=False)) == 'Ne(x, x)'
    assert Ne(x, x, evaluate=False).doit() == S.false
    assert str(Ge(x, x, evaluate=False)) == 'x >= x'
    assert str(Le(x, x, evaluate=False)) == 'x <= x'
    assert str(Gt(x, x, evaluate=False)) == 'x > x'
    assert str(Lt(x, x, evaluate=False)) == 'x < x'