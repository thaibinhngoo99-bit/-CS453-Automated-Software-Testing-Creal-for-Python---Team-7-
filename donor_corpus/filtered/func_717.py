def test_how_head_requests_are_handled(dummy_request: RequestRetval):
    app = App(__name__)

    @app.add('/foo', methods=['POST'])
    def handle_foo(request):
        return b'123'
    dummy_request.request.site = app.site
    dummy_request.channel.site = app.site
    dummy_request.request.requestReceived(b'HEAD', b'/foo', b'HTTP/1.1')
    assert dummy_request.request.code == 405
    assert dummy_request.request.code_message == b'Method not allowed'