def test_require_version_not_new_enough():
    with pytest.raises(SystemExit) as excinfo:
        autofix_lib.require_version_gte('pre-commit', '999')
    msg, = excinfo.value.args
    assert msg == f'This tool requires the `pre-commit` package is at least version 999.  The currently installed version is {PRE_COMMIT_VERSION}.\n\nTry `pip install --upgrade pre-commit`'