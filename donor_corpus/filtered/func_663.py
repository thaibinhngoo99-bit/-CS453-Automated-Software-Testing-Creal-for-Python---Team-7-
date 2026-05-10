def test_api_error(requests_mock):
    conn = Connection(API_URL)
    requests_mock.get('https://oeo.net/collections/foobar', status_code=404, json={'code': 'CollectionNotFound', 'message': "No such things as a collection 'foobar'", 'id': '54321'})
    with pytest.raises(OpenEoApiError) as exc_info:
        conn.describe_collection('foobar')
    exc = exc_info.value
    assert exc.http_status_code == 404
    assert exc.code == 'CollectionNotFound'
    assert exc.message == "No such things as a collection 'foobar'"
    assert exc.id == '54321'
    assert exc.url is None