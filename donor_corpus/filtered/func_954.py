def test_PrettyPoly():
    from sympy.polys.domains import QQ
    F = QQ.frac_field(x, y)
    R = QQ[x, y]
    assert sstr(F.convert(x / (x + y))) == sstr(x / (x + y))
    assert sstr(R.convert(x + y)) == sstr(x + y)