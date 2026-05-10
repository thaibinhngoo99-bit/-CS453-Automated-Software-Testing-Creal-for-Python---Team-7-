def test_nan_equality_exceptions():
    import random
    assert Equality(nan, nan) is S.false
    assert Unequality(nan, nan) is S.true
    A = (x, S(0), S(1) / 3, pi, oo, -oo)
    assert Equality(nan, random.choice(A)) is S.false
    assert Equality(random.choice(A), nan) is S.false
    assert Unequality(nan, random.choice(A)) is S.true
    assert Unequality(random.choice(A), nan) is S.true