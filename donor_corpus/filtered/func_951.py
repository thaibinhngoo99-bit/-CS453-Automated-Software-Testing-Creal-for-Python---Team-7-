def test_noncommutative():
    A, B, C = symbols('A,B,C', commutative=False)
    assert sstr(A * B * C ** (-1)) == 'A*B*C**(-1)'
    assert sstr(C ** (-1) * A * B) == 'C**(-1)*A*B'
    assert sstr(A * C ** (-1) * B) == 'A*C**(-1)*B'
    assert sstr(sqrt(A)) == 'sqrt(A)'
    assert sstr(1 / sqrt(A)) == 'A**(-1/2)'