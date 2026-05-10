def test_collapse_list():
    assert collapse_list([]) == ''
    assert collapse_list(['o', 'x', 'x', 'o']) == 'oxxo'
    assert collapse_list(['x', 'x', None, None, None]) == 'xx...'