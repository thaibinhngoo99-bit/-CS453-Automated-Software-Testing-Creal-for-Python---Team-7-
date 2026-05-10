def test_assert_importable_not_importable():
    with pytest.raises(SystemExit) as excinfo:
        autofix_lib.assert_importable('watmodule', install='wat')
    msg, = excinfo.value.args
    assert msg == 'This tool requires the `watmodule` module to be installed.\nTry installing it via `pip install wat`.'