def test_Float():
    assert str(Float('1.23', prec=1 + 2)) == '1.23'
    assert str(Float('1.23456789', prec=1 + 8)) == '1.23456789'
    assert str(Float('1.234567890123456789', prec=1 + 18)) == '1.234567890123456789'
    assert str(pi.evalf(1 + 2)) == '3.14'
    assert str(pi.evalf(1 + 14)) == '3.14159265358979'
    assert str(pi.evalf(1 + 64)) == '3.1415926535897932384626433832795028841971693993751058209749445923'
    assert str(pi.round(-1)) == '0.'
    assert str((pi ** 400 - (pi ** 400).round(1)).n(2)) == '-0.e+88'