def test_authenticate_basic(requests_mock):
    conn = Connection(API_URL)

    def text_callback(request, context):
        assert request.headers['Authorization'] == 'Basic am9objpqMGhu'
        return '{"access_token":"w3lc0m3"}'
    requests_mock.get('https://oeo.net/credentials/basic', text=text_callback)
    assert isinstance(conn.auth, NullAuth)
    conn.authenticate_basic(username='john', password='j0hn')
    assert isinstance(conn.auth, BearerAuth)
    assert conn.auth.bearer == 'w3lc0m3'