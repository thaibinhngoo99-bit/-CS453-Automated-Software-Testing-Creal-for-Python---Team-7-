def test_leaves_remote_addr_alone_if_no_real_ip():
    remote_addr = object()
    request = unittest.mock.MagicMock()
    request.META = {'REMOTE_ADDR': remote_addr}
    middleware.XRealIPMiddleware(get_response)(request)
    assert request.META['REMOTE_ADDR'] is remote_addr