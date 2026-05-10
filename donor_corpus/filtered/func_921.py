def test_Abs():
    assert str(Abs(x)) == 'Abs(x)'
    assert str(Abs(Rational(1, 6))) == '1/6'
    assert str(Abs(Rational(-1, 6))) == '1/6'