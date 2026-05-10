@pytest.mark.parametrize(['base', 'paths', 'expected_path'], [('https://oeo.net', ['foo', '/foo'], 'https://oeo.net/foo'), ('https://oeo.net/', ['foo', '/foo'], 'https://oeo.net/foo'), ('https://oeo.net', ['foo/', '/foo/'], 'https://oeo.net/foo/'), ('https://oeo.net/', ['foo/', '/foo/'], 'https://oeo.net/foo/'), ('https://oeo.net/api/v04', ['foo/bar', '/foo/bar'], 'https://oeo.net/api/v04/foo/bar'), ('https://oeo.net/api/v04/', ['foo/bar', '/foo/bar'], 'https://oeo.net/api/v04/foo/bar'), ('https://oeo.net/api/v04', ['foo/bar/', '/foo/bar/'], 'https://oeo.net/api/v04/foo/bar/'), ('https://oeo.net/api/v04/', ['foo/bar/', '/foo/bar/'], 'https://oeo.net/api/v04/foo/bar/')])
def test_rest_api_connection_url_handling(requests_mock, base, paths, expected_path):
    """Test connection __init__ and proper joining of root url and API path"""
    conn = RestApiConnection(base)
    requests_mock.get(expected_path, text='payload')
    requests_mock.post(expected_path, text='payload')
    for path in paths:
        assert conn.get(path).text == 'payload'
        assert conn.post(path, {'foo': 'bar'}).text == 'payload'