def test_GroebnerBasis():
    assert str(groebner([], x, y)) == "GroebnerBasis([], x, y, domain='ZZ', order='lex')"
    F = [x ** 2 - 3 * y - x + 1, y ** 2 - 2 * x + y - 1]
    assert str(groebner(F, order='grlex')) == "GroebnerBasis([x**2 - x - 3*y + 1, y**2 - 2*x + y - 1], x, y, domain='ZZ', order='grlex')"
    assert str(groebner(F, order='lex')) == "GroebnerBasis([2*x - y**2 - y + 1, y**4 + 2*y**3 - 3*y**2 - 16*y + 7], x, y, domain='ZZ', order='lex')"