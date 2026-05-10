def test_connection_with_session():
    session = mock.Mock()
    response = session.request.return_value
    response.status_code = 200
    response.json.return_value = {'foo': 'bar'}
    conn = Connection('https://oeo.net/', session=session)
    assert conn.capabilities().capabilities == {'foo': 'bar'}
    session.request.assert_any_call(url='https://oeo.net/', method='get', headers=mock.ANY, stream=mock.ANY, auth=mock.ANY)