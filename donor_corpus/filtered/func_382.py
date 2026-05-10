@pytest.mark.asyncio
async def test_lock_already_locked(monkeypatch):
    """Test lock() when already locked."""
    _mock = TeslaMock(monkeypatch)
    _controller = Controller(None)
    _data = _mock.data_request_vehicle()
    _data['vehicle_state']['rt'] = 0
    _lock = TrunkLock(_data, _controller)
    await _lock.async_update()
    await _lock.lock()
    assert _lock is not None
    assert _lock.is_locked()