def test_has_battery(monkeypatch):
    """Test has_battery()."""
    _mock = TeslaMock(monkeypatch)
    _controller = Controller(None)
    _data = _mock.data_request_vehicle()
    _lock = TrunkLock(_data, _controller)
    assert not _lock.has_battery()