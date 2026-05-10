def test_interactive_no(mock_input, capfd):
    mock_input.set_side_effect('n')
    assert autofix_lib._interactive_check(use_color=False) is False
    out, _ = capfd.readouterr()
    assert out == '***Looks good [y,n,s,q,?]? <<n\n'