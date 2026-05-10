def test_categories():
    from sympy.categories import Object, Morphism, NamedMorphism, IdentityMorphism, Category
    A = Object('A')
    B = Object('B')
    f = NamedMorphism(A, B, 'f')
    id_A = IdentityMorphism(A)
    K = Category('K')
    assert str(A) == 'Object("A")'
    assert str(f) == 'NamedMorphism(Object("A"), Object("B"), "f")'
    assert str(id_A) == 'IdentityMorphism(Object("A"))'
    assert str(K) == 'Category("K")'