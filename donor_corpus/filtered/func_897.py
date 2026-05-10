def test_equals():
    w, x, y, z = symbols('w:z')
    f = Function('f')
    assert Eq(x, 1).equals(Eq(x * (y + 1) - x * y - x + 1, x))
    assert Eq(x, y).equals(x < y, True) == False
    assert Eq(x, f(1)).equals(Eq(x, f(2)), True) == f(1) - f(2)
    assert Eq(f(1), y).equals(Eq(f(2), y), True) == f(1) - f(2)
    assert Eq(x, f(1)).equals(Eq(f(2), x), True) == f(1) - f(2)
    assert Eq(f(1), x).equals(Eq(x, f(2)), True) == f(1) - f(2)
    assert Eq(w, x).equals(Eq(y, z), True) == False
    assert Eq(f(1), f(2)).equals(Eq(f(3), f(4)), True) == f(1) - f(3)
    assert (x < y).equals(y > x, True) == True
    assert (x < y).equals(y >= x, True) == False
    assert (x < y).equals(z < y, True) == False
    assert (x < y).equals(x < z, True) == False
    assert (x < f(1)).equals(x < f(2), True) == f(1) - f(2)
    assert (f(1) < x).equals(f(2) < x, True) == f(1) - f(2)