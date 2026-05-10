def test_Function():
    f = Function('f')
    fx = f(x)
    w = WildFunction('w')
    assert str(f) == 'f'
    assert str(fx) == 'f(x)'
    assert str(w) == 'w_'