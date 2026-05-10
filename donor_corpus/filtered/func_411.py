def test_cwd(tmpdir):
    orig = os.getcwd()
    with autofix_lib.cwd(tmpdir):
        assert os.getcwd() == tmpdir
    assert os.getcwd() == orig