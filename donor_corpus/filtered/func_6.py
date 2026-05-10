@httpretty.activate
def test_timeout():
    httpretty.register_uri(httpretty.POST, 'http://example.com/RPC2', content_type='text/xml', body=timeout)
    proxy = ServerProxy('http://example.com', timeout=0.5)
    with pytest.raises(socket.timeout):
        proxy.test()