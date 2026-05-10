def test_Rational():
    n1 = Rational(1, 4)
    n2 = Rational(1, 3)
    n3 = Rational(2, 4)
    n4 = Rational(2, -4)
    n5 = Rational(0)
    n6 = Rational(1)
    n7 = Rational(3)
    n8 = Rational(-3)
    assert str(n1 * n2) == '1/12'
    assert str(n1 * n2) == '1/12'
    assert str(n3) == '1/2'
    assert str(n1 * n3) == '1/8'
    assert str(n1 + n3) == '3/4'
    assert str(n1 + n2) == '7/12'
    assert str(n1 + n4) == '-1/4'
    assert str(n4 * n4) == '1/4'
    assert str(n4 + n2) == '-1/6'
    assert str(n4 + n5) == '-1/2'
    assert str(n4 * n5) == '0'
    assert str(n3 + n4) == '0'
    assert str(n1 ** n7) == '1/64'
    assert str(n2 ** n7) == '1/27'
    assert str(n2 ** n8) == '27'
    assert str(n7 ** n8) == '1/27'
    assert str(Rational('-25')) == '-25'
    assert str(Rational('1.25')) == '5/4'
    assert str(Rational('-2.6e-2')) == '-13/500'
    assert str(S('25/7')) == '25/7'
    assert str(S('-123/569')) == '-123/569'
    assert str(S('0.1[23]', rational=1)) == '61/495'
    assert str(S('5.1[666]', rational=1)) == '31/6'
    assert str(S('-5.1[666]', rational=1)) == '-31/6'
    assert str(S('0.[9]', rational=1)) == '1'
    assert str(S('-0.[9]', rational=1)) == '-1'
    assert str(sqrt(Rational(1, 4))) == '1/2'
    assert str(sqrt(Rational(1, 36))) == '1/6'
    assert str((123 ** 25) ** Rational(1, 25)) == '123'
    assert str((123 ** 25 + 1) ** Rational(1, 25)) != '123'
    assert str((123 ** 25 - 1) ** Rational(1, 25)) != '123'
    assert str((123 ** 25 - 1) ** Rational(1, 25)) != '122'
    assert str(sqrt(Rational(81, 36)) ** 3) == '27/8'
    assert str(1 / sqrt(Rational(81, 36)) ** 3) == '8/27'
    assert str(sqrt(-4)) == str(2 * I)
    assert str(2 ** Rational(1, 10 ** 10)) == '2**(1/10000000000)'