def test_authenticate_oidc(oidc_test_setup):
    client_id = 'myclient'
    oidc_discovery_url = 'https://oeo.net/credentials/oidc'
    state, webbrowser_open = oidc_test_setup(client_id=client_id, oidc_discovery_url=oidc_discovery_url)
    conn = Connection(API_URL)
    assert isinstance(conn.auth, NullAuth)
    conn.authenticate_OIDC(client_id=client_id, webbrowser_open=webbrowser_open)
    assert isinstance(conn.auth, BearerAuth)
    assert conn.auth.bearer == state['access_token']