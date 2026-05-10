def test_set():
    assert sstr(set()) == 'set()'
    assert sstr(frozenset()) == 'frozenset()'
    assert sstr(set([1, 2, 3])) == 'set([1, 2, 3])'
    assert sstr(set([1, x, x ** 2, x ** 3, x ** 4])) == 'set([1, x, x**2, x**3, x**4])'