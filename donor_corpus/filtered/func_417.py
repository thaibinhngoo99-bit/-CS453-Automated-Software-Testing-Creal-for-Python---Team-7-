def test_interactive_yes(mock_input, capfd):
    mock_input.set_side_effect('y')
    assert autofix_lib._interactive_check(use_color=False) is True
    out, _ = capfd.readouterr()
    assert out == '***Looks good [y,n,s,q,?]? <<y\n'