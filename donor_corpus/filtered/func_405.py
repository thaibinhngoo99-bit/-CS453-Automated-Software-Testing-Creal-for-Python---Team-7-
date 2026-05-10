def test_replace_all_in_matrix():
    assert replace_all_in_matrix([[1, 2, 3, 'n', 'n', None], [4, 5, 'n']], 'n', '#') == [[1, 2, 3, '#', '#', None], [4, 5, '#']]
    assert replace_all_in_matrix([[None, None, 2, True], [4, 5, '#']], 'k', 42) == [[None, None, 2, True], [4, 5, '#']]
    assert replace_all_in_matrix([], None, 7) == []
    assert replace_all_in_matrix([[], []], None, 7) == [[], []]