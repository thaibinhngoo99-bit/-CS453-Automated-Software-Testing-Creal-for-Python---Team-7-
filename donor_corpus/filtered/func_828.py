def test_text_input_controls_explicit():
    text_input = TextInput()
    controls = text_input.controls(['placeholder', 'disabled'])
    assert isinstance(controls, WidgetBox)
    assert len(controls) == 3
    name, disabled, placeholder = controls
    assert isinstance(name, StaticText)
    assert isinstance(disabled, Checkbox)
    assert isinstance(placeholder, TextInput)
    text_input.disabled = True
    assert disabled.value
    text_input.placeholder = 'Test placeholder...'
    assert placeholder.value == 'Test placeholder...'