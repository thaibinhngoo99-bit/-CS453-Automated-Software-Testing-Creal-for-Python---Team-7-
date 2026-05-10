@XFAIL
def test_issue_8444():
    x = symbols('x', real=True)
    assert (x <= oo) == (x >= -oo) == True
    x = symbols('x')
    assert x >= floor(x)
    assert (x < floor(x)) == False
    assert Gt(x, floor(x)) == Gt(x, floor(x), evaluate=False)
    assert Ge(x, floor(x)) == Ge(x, floor(x), evaluate=False)
    assert x <= ceiling(x)
    assert (x > ceiling(x)) == False
    assert Lt(x, ceiling(x)) == Lt(x, ceiling(x), evaluate=False)
    assert Le(x, ceiling(x)) == Le(x, ceiling(x), evaluate=False)
    i = symbols('i', integer=True)
    assert (i > floor(i)) == False
    assert (i < ceiling(i)) == False