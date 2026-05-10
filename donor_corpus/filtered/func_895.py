def test_issue_8245():
    a = S('6506833320952669167898688709329/5070602400912917605986812821504')
    q = a.n(10)
    assert (a == q) is True
    assert (a != q) is False
    assert (a > q) == False
    assert (a < q) == False
    assert (a >= q) == True
    assert (a <= q) == True
    a = sqrt(2)
    r = Rational(str(a.n(30)))
    assert (r == a) is False
    assert (r != a) is True
    assert (r > a) == True
    assert (r < a) == False
    assert (r >= a) == True
    assert (r <= a) == False
    a = sqrt(2)
    r = Rational(str(a.n(29)))
    assert (r == a) is False
    assert (r != a) is True
    assert (r > a) == False
    assert (r < a) == True
    assert (r >= a) == False
    assert (r <= a) == True