def test_relational_bool_output():
    raises(TypeError, lambda: bool(x > 3))
    raises(TypeError, lambda: bool(x >= 3))
    raises(TypeError, lambda: bool(x < 3))
    raises(TypeError, lambda: bool(x <= 3))
    raises(TypeError, lambda: bool(Eq(x, 3)))
    raises(TypeError, lambda: bool(Ne(x, 3)))