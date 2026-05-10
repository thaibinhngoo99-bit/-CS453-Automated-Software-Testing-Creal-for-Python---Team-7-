@pytest.mark.asyncio
async def test_is_locked_after_update(monkeypatch):
    """Test is_locked() after an update."""
    _mock = TeslaMock(monkeypatch)
    _controller = Controller(None)
    _data = _mock.data_request_vehicle()
    _data['vehicle_state']['rt'] = 0
    _lock = TrunkLock(_data, _controller)
    await _lock.async_update()
    assert _lock is not None
    assert _lock.is_locked()