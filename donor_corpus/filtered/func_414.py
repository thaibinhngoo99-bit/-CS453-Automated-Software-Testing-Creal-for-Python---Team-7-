def test_interactive_control_c(mock_input, capfd):
    mock_input.set_side_effect(KeyboardInterrupt)
    with pytest.raises(SystemExit):
        autofix_lib._interactive_check(use_color=False)
    out, _ = capfd.readouterr()
    assert out == '***Looks good [y,n,s,q,?]? ^C\nGoodbye!\n'