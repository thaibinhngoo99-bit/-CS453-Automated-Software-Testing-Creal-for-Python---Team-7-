def test_Mul():
    assert str(x / y) == 'x/y'
    assert str(y / x) == 'y/x'
    assert str(x / y / z) == 'x/(y*z)'
    assert str((x + 1) / (y + 2)) == '(x + 1)/(y + 2)'
    assert str(2 * x / 3) == '2*x/3'
    assert str(-2 * x / 3) == '-2*x/3'

    class CustomClass1(Expr):
        is_commutative = True

    class CustomClass2(Expr):
        is_commutative = True
    cc1 = CustomClass1()
    cc2 = CustomClass2()
    assert str(Rational(2) * cc1) == '2*CustomClass1()'
    assert str(cc1 * Rational(2)) == '2*CustomClass1()'
    assert str(cc1 * Float('1.5')) == '1.5*CustomClass1()'
    assert str(cc2 * Rational(2)) == '2*CustomClass2()'
    assert str(cc2 * Rational(2) * cc1) == '2*CustomClass1()*CustomClass2()'
    assert str(cc1 * Rational(2) * cc2) == '2*CustomClass1()*CustomClass2()'