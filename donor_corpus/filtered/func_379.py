@pytest.mark.asyncio
async def test_unlock(monkeypatch):
    """Test unlock()."""
    _mock = TeslaMock(monkeypatch)
    _controller = Controller(None)
    _data = _mock.data_request_vehicle()
    _data['vehicle_state']['rt'] = 0
    _lock = TrunkLock(_data, _controller)
    await _lock.async_update()
    await _lock.unlock()
    assert _lock is not None
    assert not _lock.is_locked()