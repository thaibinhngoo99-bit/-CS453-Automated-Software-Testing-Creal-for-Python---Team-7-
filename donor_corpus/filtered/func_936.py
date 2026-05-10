def test_Poly():
    assert str(Poly(0, x)) == "Poly(0, x, domain='ZZ')"
    assert str(Poly(1, x)) == "Poly(1, x, domain='ZZ')"
    assert str(Poly(x, x)) == "Poly(x, x, domain='ZZ')"
    assert str(Poly(2 * x + 1, x)) == "Poly(2*x + 1, x, domain='ZZ')"
    assert str(Poly(2 * x - 1, x)) == "Poly(2*x - 1, x, domain='ZZ')"
    assert str(Poly(-1, x)) == "Poly(-1, x, domain='ZZ')"
    assert str(Poly(-x, x)) == "Poly(-x, x, domain='ZZ')"
    assert str(Poly(-2 * x + 1, x)) == "Poly(-2*x + 1, x, domain='ZZ')"
    assert str(Poly(-2 * x - 1, x)) == "Poly(-2*x - 1, x, domain='ZZ')"
    assert str(Poly(x - 1, x)) == "Poly(x - 1, x, domain='ZZ')"
    assert str(Poly(x ** 2 + 1 + y, x)) == "Poly(x**2 + y + 1, x, domain='ZZ[y]')"
    assert str(Poly(x ** 2 - 1 + y, x)) == "Poly(x**2 + y - 1, x, domain='ZZ[y]')"
    assert str(Poly(x ** 2 + I * x, x)) == "Poly(x**2 + I*x, x, domain='EX')"
    assert str(Poly(x ** 2 - I * x, x)) == "Poly(x**2 - I*x, x, domain='EX')"
    assert str(Poly(-x * y * z + x * y - 1, x, y, z)) == "Poly(-x*y*z + x*y - 1, x, y, z, domain='ZZ')"
    assert str(Poly(-w * x ** 21 * y ** 7 * z + (1 + w) * z ** 3 - 2 * x * z + 1, x, y, z)) == "Poly(-w*x**21*y**7*z - 2*x*z + (w + 1)*z**3 + 1, x, y, z, domain='ZZ[w]')"
    assert str(Poly(x ** 2 + 1, x, modulus=2)) == 'Poly(x**2 + 1, x, modulus=2)'
    assert str(Poly(2 * x ** 2 + 3 * x + 4, x, modulus=17)) == 'Poly(2*x**2 + 3*x + 4, x, modulus=17)'