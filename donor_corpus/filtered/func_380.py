@pytest.mark.asyncio
async def test_unlock_already_unlocked(monkeypatch):
    """Test unlock() when already unlocked."""
    _mock = TeslaMock(monkeypatch)
    _controller = Controller(None)
    _data = _mock.data_request_vehicle()
    _data['vehicle_state']['rt'] = 123
    _lock = TrunkLock(_data, _controller)
    await _lock.async_update()
    await _lock.unlock()
    assert _lock is not None
    assert not _lock.is_locked()
    _data['vehicle_state']['rt'] = 0