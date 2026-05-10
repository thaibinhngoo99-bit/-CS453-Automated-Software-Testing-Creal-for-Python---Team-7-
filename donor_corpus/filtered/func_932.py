def test_Matrix():
    M = Matrix([[x ** (+1), 1], [y, x + y]])
    assert str(M) == sstr(M) == '[x,     1]\n[y, x + y]'
    M = Matrix()
    assert str(M) == sstr(M) == '[]'
    M = Matrix(0, 1, lambda i, j: 0)
    assert str(M) == sstr(M) == '[]'