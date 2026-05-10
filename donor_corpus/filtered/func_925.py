def test_Dict():
    assert str(Dict({1: 1 + x})) == sstr({1: 1 + x}) == '{1: x + 1}'
    assert str(Dict({1: x ** 2, 2: y * x})) in ('{1: x**2, 2: x*y}', '{2: x*y, 1: x**2}')
    assert sstr(Dict({1: x ** 2, 2: y * x})) == '{1: x**2, 2: x*y}'