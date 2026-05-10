def test_Tr():
    A, B = symbols('A B', commutative=False)
    t = Tr(A * B)
    assert str(t) == 'Tr(A*B)'