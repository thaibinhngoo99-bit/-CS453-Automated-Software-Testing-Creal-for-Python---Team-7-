def test_Interval():
    a = Symbol('a', real=True)
    assert str(Interval(0, a)) == '[0, a]'
    assert str(Interval(0, a, False, False)) == '[0, a]'
    assert str(Interval(0, a, True, False)) == '(0, a]'
    assert str(Interval(0, a, False, True)) == '[0, a)'
    assert str(Interval(0, a, True, True)) == '(0, a)'