def test_handle_add_slashes(dummy_request: RequestRetval):
    app = App(__name__)
    mock = MagicMock()
    app.route('/js/')(mock)
    dummy_request.request.site = app.site
    dummy_request.channel.site = app.site
    dummy_request.request.requestReceived(b'GET', b'/js', b'HTTP/1.1')
    assert dummy_request.request.code == 308
    assert dummy_request.request.code_message == b'Permanent Redirect'
    assert dummy_request.request.responseHeaders.getRawHeaders(b'location') == [b'http://10.0.0.1/js/']
    assert mock.call_count == 0