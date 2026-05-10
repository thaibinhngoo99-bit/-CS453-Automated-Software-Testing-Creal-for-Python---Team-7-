@pytest.mark.parametrize('attribute_name, attribute_value', [('current_direction', 'forward'), ('oscillating', True), ('percentage', 50), ('preset_mode', 'medium'), ('preset_modes', ['low', 'medium', 'high']), ('speed_count', 50), ('supported_features', 1)])
def test_fanentity_attributes(attribute_name, attribute_value):
    """Test fan entity attribute shorthand."""
    fan = BaseFan()
    setattr(fan, f'_attr_{attribute_name}', attribute_value)
    assert getattr(fan, attribute_name) == attribute_value