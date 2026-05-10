def test_replace_all_in_list():
    assert replace_all_in_list([None, 3, '546', 33, None], None, '#') == ['#', 3, '546', 33, '#']
    assert replace_all_in_list([1, 2, 3, 4, 5], 'e', 42) == [1, 2, 3, 4, 5]
    assert replace_all_in_list([], 34, 43) == []