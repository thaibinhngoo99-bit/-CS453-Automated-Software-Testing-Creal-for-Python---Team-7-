def test_tuple():
    assert str((x,)) == sstr((x,)) == '(x,)'
    assert str((x + y, 1 + x)) == sstr((x + y, 1 + x)) == '(x + y, x + 1)'
    assert str((x + y, (1 + x, x ** 2))) == sstr((x + y, (1 + x, x ** 2))) == '(x + y, (x + 1, x**2))'