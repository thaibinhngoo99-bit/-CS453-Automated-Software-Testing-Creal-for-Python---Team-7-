def test_Order():
    assert str(O(x)) == 'O(x)'
    assert str(O(x ** 2)) == 'O(x**2)'
    assert str(O(x * y)) == 'O(x*y, x, y)'