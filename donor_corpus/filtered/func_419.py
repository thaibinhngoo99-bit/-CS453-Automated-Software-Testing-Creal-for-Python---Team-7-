def test_interactive_shell(mock_input, capfd):
    mock_input.set_side_effect('s', 'n')
    with mock.patch.dict(os.environ, {'SHELL': 'echo'}):
        assert autofix_lib._interactive_check(use_color=False) is False
    out, _ = capfd.readouterr()
    assert out == '***Looks good [y,n,s,q,?]? <<s\nOpening an interactive shell, type `exit` to continue.\nAny modifications will be committed.\n\n***Looks good [y,n,s,q,?]? <<n\n'