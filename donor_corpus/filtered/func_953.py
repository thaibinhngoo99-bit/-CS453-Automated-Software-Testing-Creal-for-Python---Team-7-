def test_RandomDomain():
    from sympy.stats import Normal, Die, Exponential, pspace, where
    X = Normal('x1', 0, 1)
    assert str(where(X > 0)) == 'Domain: 0 < x1'
    D = Die('d1', 6)
    assert str(where(D > 4)) == 'Domain: Or(d1 == 5, d1 == 6)'
    A = Exponential('a', 1)
    B = Exponential('b', 1)
    assert str(pspace(Tuple(A, B)).domain) == 'Domain: And(0 <= a, 0 <= b)'