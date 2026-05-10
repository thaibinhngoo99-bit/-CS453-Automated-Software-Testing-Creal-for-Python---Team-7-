def test_complex_compare_not_real():
    y = Symbol('y', imaginary=True)
    z = Symbol('z', complex=True, real=False)
    for w in (y, z):
        assert_all_ineq_raise_TypeError(2, w)
    t = Symbol('t')
    x = Symbol('x', real=True)
    z = Symbol('z', complex=True)
    for w in (x, z, t):
        assert_all_ineq_give_class_Inequality(2, w)