def test_complex_pure_imag_not_ordered():
    raises(TypeError, lambda: 2 * I < 3 * I)
    x = Symbol('x', real=True, nonzero=True)
    y = Symbol('y', imaginary=True)
    z = Symbol('z', complex=True)
    assert_all_ineq_raise_TypeError(I, y)
    t = I * x
    assert_all_ineq_raise_TypeError(2, t)
    t = -I * y
    assert_all_ineq_give_class_Inequality(2, t)
    t = I * z
    assert_all_ineq_give_class_Inequality(2, t)