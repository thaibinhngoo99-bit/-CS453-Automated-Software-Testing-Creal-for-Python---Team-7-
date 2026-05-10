def test_Not():
    assert Not(Equality(x, y)) == Unequality(x, y)
    assert Not(Unequality(x, y)) == Equality(x, y)
    assert Not(StrictGreaterThan(x, y)) == LessThan(x, y)
    assert Not(StrictLessThan(x, y)) == GreaterThan(x, y)
    assert Not(GreaterThan(x, y)) == StrictLessThan(x, y)
    assert Not(LessThan(x, y)) == StrictGreaterThan(x, y)