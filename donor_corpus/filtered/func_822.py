def test_reactive_servable_title():
    doc = Document()
    session_context = unittest.mock.Mock()
    with patch_curdoc(doc):
        doc._session_context = lambda: session_context
        ReactiveHTML().servable(title='A')
        ReactiveHTML().servable(title='B')
    assert doc.title == 'B'