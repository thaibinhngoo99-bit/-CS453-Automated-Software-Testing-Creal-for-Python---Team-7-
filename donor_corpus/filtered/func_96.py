@pytest.mark.parametrize('backend', _get_testable_interactive_backends())
@pytest.mark.parametrize('toolbar', ['toolbar2', 'toolmanager'])
@pytest.mark.flaky(reruns=3)
def test_interactive_backend(backend, toolbar):
    if backend == 'macosx':
        if toolbar == 'toolmanager':
            pytest.skip('toolmanager is not implemented for macosx.')
        if toolbar == 'toolbar2' and os.environ.get('TRAVIS'):
            pytest.skip('toolbar2 for macosx is buggy on Travis.')
    proc = subprocess.run([sys.executable, '-c', _test_script, json.dumps({'toolbar': toolbar})], env={**os.environ, 'MPLBACKEND': backend, 'SOURCE_DATE_EPOCH': '0'}, timeout=_test_timeout, stdout=subprocess.PIPE, universal_newlines=True)
    if proc.returncode:
        pytest.fail(f'The subprocess returned with non-zero exit status {proc.returncode}.')
    assert proc.stdout.count('CloseEvent') == 1