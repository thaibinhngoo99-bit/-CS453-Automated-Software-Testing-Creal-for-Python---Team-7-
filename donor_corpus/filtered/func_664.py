def test_api_error_non_json(requests_mock):
    conn = Connection(API_URL)
    requests_mock.get('https://oeo.net/collections/foobar', status_code=500, text='olapola')
    with pytest.raises(OpenEoApiError) as exc_info:
        conn.describe_collection('foobar')
    exc = exc_info.value
    assert exc.http_status_code == 500
    assert exc.code == 'unknown'
    assert exc.message == 'olapola'
    assert exc.id is None
    assert exc.url is None