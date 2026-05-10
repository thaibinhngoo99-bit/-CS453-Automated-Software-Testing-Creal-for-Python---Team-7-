async def test_async_fanentity(hass):
    """Test async fan entity methods."""
    fan = BaseFan()
    fan.hass = hass
    assert fan.state == 'off'
    assert fan.preset_modes is None
    assert fan.supported_features == 0
    assert fan.percentage_step == 1
    assert fan.speed_count == 100
    assert fan.capability_attributes == {}
    with pytest.raises(NotImplementedError):
        await fan.async_oscillate(True)
    with pytest.raises(AttributeError):
        await fan.async_set_speed('low')
    with pytest.raises(NotImplementedError):
        await fan.async_set_percentage(0)
    with pytest.raises(NotImplementedError):
        await fan.async_set_preset_mode('auto')
    with pytest.raises(NotImplementedError):
        await fan.async_turn_on()
    with pytest.raises(NotImplementedError):
        await fan.async_turn_off()
    with pytest.raises(NotImplementedError):
        await fan.async_increase_speed()
    with pytest.raises(NotImplementedError):
        await fan.async_decrease_speed()