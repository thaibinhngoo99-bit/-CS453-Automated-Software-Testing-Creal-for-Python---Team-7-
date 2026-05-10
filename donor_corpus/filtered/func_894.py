def test_ineq_avoid_wild_symbol_flip():
    from sympy.core.symbol import Wild
    p = symbols('p', cls=Wild)
    assert Gt(x, p) == Gt(x, p, evaluate=False)
    e = Lt(x, y).subs({y: p})
    assert e == Lt(x, p, evaluate=False)
    e = Ge(x, p).doit()
    assert e == Ge(x, p, evaluate=False)