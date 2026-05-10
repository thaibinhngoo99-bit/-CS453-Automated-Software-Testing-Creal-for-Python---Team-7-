def test_text_input_controls():
    text_input = TextInput()
    controls = text_input.controls()
    assert isinstance(controls, Tabs)
    assert len(controls) == 2
    wb1, wb2 = controls
    assert isinstance(wb1, WidgetBox)
    assert len(wb1) == 6
    name, disabled, *ws = wb1
    assert isinstance(name, StaticText)
    assert isinstance(disabled, Checkbox)
    not_checked = []
    for w in ws:
        if w.name == 'Value':
            assert isinstance(w, TextInput)
            text_input.value = 'New value'
            assert w.value == 'New value'
        elif w.name == 'Value input':
            assert isinstance(w, TextInput)
        elif w.name == 'Placeholder':
            assert isinstance(w, TextInput)
            text_input.placeholder = 'Test placeholder...'
            assert w.value == 'Test placeholder...'
        elif w.name == 'Max length':
            assert isinstance(w, IntInput)
        else:
            not_checked.append(w)
    assert not not_checked
    assert isinstance(wb2, WidgetBox)
    assert len(wb2) == len(list(Viewable.param)) + 1