def test_run(capfd):
    autofix_lib.run('echo', 'h"i')
    out, _ = capfd.readouterr()
    assert out == '$ echo \'h"i\'\nh"i\n'