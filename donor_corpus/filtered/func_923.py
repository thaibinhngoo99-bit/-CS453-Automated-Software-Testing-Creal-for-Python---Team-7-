def test_Derivative():
    assert str(Derivative(x, y)) == 'Derivative(x, y)'
    assert str(Derivative(x ** 2, x, evaluate=False)) == 'Derivative(x**2, x)'
    assert str(Derivative(x ** 2 / y, x, y, evaluate=False)) == 'Derivative(x**2/y, x, y)'