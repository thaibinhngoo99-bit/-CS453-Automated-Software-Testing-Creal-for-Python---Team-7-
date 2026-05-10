def test_is_locked_on_init(monkeypatch):
    """Test is_locked() after initialization."""
    _mock = TeslaMock(monkeypatch)
    _controller = Controller(None)
    _data = _mock.data_request_vehicle()
    _lock = TrunkLock(_data, _controller)
    assert _lock is not None
    assert not _lock.is_locked()