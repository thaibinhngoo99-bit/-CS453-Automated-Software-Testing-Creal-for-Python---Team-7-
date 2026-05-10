def test_factorial():
    n = Symbol('n', integer=True)
    assert str(factorial(-2)) == '0'
    assert str(factorial(0)) == '1'
    assert str(factorial(7)) == '5040'
    assert str(factorial(n)) == 'n!'
    assert str(factorial(2 * n)) == '(2*n)!'
    assert str(factorial(factorial(n))) == '(n!)!'
    assert str(factorial(factorial2(n))) == '(n!!)!'
    assert str(factorial2(factorial(n))) == '(n!)!!'
    assert str(factorial2(factorial2(n))) == '(n!!)!!'