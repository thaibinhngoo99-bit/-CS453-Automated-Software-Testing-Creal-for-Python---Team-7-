def test_interactive_help(mock_input, capfd):
    mock_input.set_side_effect('?', 'n')
    assert autofix_lib._interactive_check(use_color=False) is False
    out, _ = capfd.readouterr()
    assert out == '***Looks good [y,n,s,q,?]? <<?\ny (yes): yes it looks good, commit and continue.\nn (no): no, do not commit this repository.\ns (shell): open an interactive shell in the repo.\nq (quit, ^C): early exit from the autofixer.\n? (help): show this help message.\n***Looks good [y,n,s,q,?]? <<n\n'