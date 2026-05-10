def test_inequalities_cant_sympify_other():
    from operator import gt, lt, ge, le
    bar = 'foo'
    for a in (x, S(0), S(1) / 3, pi, I, zoo, oo, -oo, nan):
        for op in (lt, gt, le, ge):
            raises(TypeError, lambda: op(a, bar))