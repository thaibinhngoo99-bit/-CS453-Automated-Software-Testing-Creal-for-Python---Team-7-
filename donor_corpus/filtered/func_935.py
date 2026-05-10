def test_Permutation_Cycle():
    from sympy.combinatorics import Permutation, Cycle
    for p, s in [(Cycle(), 'Cycle()'), (Cycle(2), 'Cycle(2)'), (Cycle(2, 1), 'Cycle(1, 2)'), (Cycle(1, 2)(5)(6, 7)(10), 'Cycle(1, 2)(6, 7)(10)'), (Cycle(3, 4)(1, 2)(3, 4), 'Cycle(1, 2)(4)')]:
        assert str(p) == s
    Permutation.print_cyclic = False
    for p, s in [(Permutation([]), 'Permutation([])'), (Permutation([], size=1), 'Permutation([0])'), (Permutation([], size=2), 'Permutation([0, 1])'), (Permutation([], size=10), 'Permutation([], size=10)'), (Permutation([1, 0, 2]), 'Permutation([1, 0, 2])'), (Permutation([1, 0, 2, 3, 4, 5]), 'Permutation([1, 0], size=6)'), (Permutation([1, 0, 2, 3, 4, 5], size=10), 'Permutation([1, 0], size=10)')]:
        assert str(p) == s
    Permutation.print_cyclic = True
    for p, s in [(Permutation([]), 'Permutation()'), (Permutation([], size=1), 'Permutation(0)'), (Permutation([], size=2), 'Permutation(1)'), (Permutation([], size=10), 'Permutation(9)'), (Permutation([1, 0, 2]), 'Permutation(2)(0, 1)'), (Permutation([1, 0, 2, 3, 4, 5]), 'Permutation(5)(0, 1)'), (Permutation([1, 0, 2, 3, 4, 5], size=10), 'Permutation(9)(0, 1)'), (Permutation([0, 1, 3, 2, 4, 5], size=10), 'Permutation(9)(2, 3)')]:
        assert str(p) == s