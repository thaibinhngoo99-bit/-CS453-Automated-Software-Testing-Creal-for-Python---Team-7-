@httpretty.activate
def test_timeout_https():
    httpretty.register_uri(httpretty.POST, 'https://example.com/RPC2', content_type='text/xml', body=timeout)
    proxy = ServerProxy('https://example.com', timeout=0.5)
    with pytest.raises(socket.timeout):
        proxy.test()