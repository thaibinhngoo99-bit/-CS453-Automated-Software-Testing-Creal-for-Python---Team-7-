def test_fanentity():
    """Test fan entity methods."""
    fan = BaseFan()
    assert fan.state == 'off'
    assert fan.preset_modes is None
    assert fan.supported_features == 0
    assert fan.percentage_step == 1
    assert fan.speed_count == 100
    assert fan.capability_attributes == {}
    with pytest.raises(NotImplementedError):
        fan.oscillate(True)
    with pytest.raises(AttributeError):
        fan.set_speed('low')
    with pytest.raises(NotImplementedError):
        fan.set_percentage(0)
    with pytest.raises(NotImplementedError):
        fan.set_preset_mode('auto')
    with pytest.raises(NotImplementedError):
        fan.turn_on()
    with pytest.raises(NotImplementedError):
        fan.turn_off()