def test_interactive_eof(mock_input, capfd):
    mock_input.set_side_effect(EOFError)
    with pytest.raises(SystemExit):
        autofix_lib._interactive_check(use_color=False)
    out, _ = capfd.readouterr()
    assert out == '***Looks good [y,n,s,q,?]? ^D\nGoodbye!\n'