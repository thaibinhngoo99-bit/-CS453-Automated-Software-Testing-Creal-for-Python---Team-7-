def test_sqrt():
    assert str(sqrt(x)) == 'sqrt(x)'
    assert str(sqrt(x ** 2)) == 'sqrt(x**2)'
    assert str(1 / sqrt(x)) == '1/sqrt(x)'
    assert str(1 / sqrt(x ** 2)) == '1/sqrt(x**2)'
    assert str(y / sqrt(x)) == 'y/sqrt(x)'
    assert str(x ** (1 / 2)) == 'x**0.5'
    assert str(1 / x ** (1 / 2)) == 'x**(-0.5)'