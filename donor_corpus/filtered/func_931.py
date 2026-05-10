def test_list():
    assert str([x]) == sstr([x]) == '[x]'
    assert str([x ** 2, x * y + 1]) == sstr([x ** 2, x * y + 1]) == '[x**2, x*y + 1]'
    assert str([x ** 2, [y + x]]) == sstr([x ** 2, [y + x]]) == '[x**2, [x + y]]'