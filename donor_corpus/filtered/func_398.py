def test_transpose():
    original = [[0, 7, 3], [4, 0, 1]]
    transposed = [[0, 4], [7, 0], [3, 1]]
    assert transpose(original) == transposed
    assert transpose(transpose(original)) == original