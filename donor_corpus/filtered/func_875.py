def test_bool():
    assert Eq(0, 0) is S.true
    assert Eq(1, 0) is S.false
    assert Ne(0, 0) is S.false
    assert Ne(1, 0) is S.true
    assert Lt(0, 1) is S.true
    assert Lt(1, 0) is S.false
    assert Le(0, 1) is S.true
    assert Le(1, 0) is S.false
    assert Le(0, 0) is S.true
    assert Gt(1, 0) is S.true
    assert Gt(0, 1) is S.false
    assert Ge(1, 0) is S.true
    assert Ge(0, 1) is S.false
    assert Ge(1, 1) is S.true
    assert Eq(I, 2) is S.false
    assert Ne(I, 2) is S.true
    raises(TypeError, lambda: Gt(I, 2))
    raises(TypeError, lambda: Ge(I, 2))
    raises(TypeError, lambda: Lt(I, 2))
    raises(TypeError, lambda: Le(I, 2))
    a = Float('.000000000000000000001', '')
    b = Float('.0000000000000000000001', '')
    assert Eq(pi + a, pi + b) is S.false