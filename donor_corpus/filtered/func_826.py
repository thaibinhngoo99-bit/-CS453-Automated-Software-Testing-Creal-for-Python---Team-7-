def test_link_properties_server(document):

    class ReactiveLink(Reactive):
        text = param.String(default='A')
    obj = ReactiveLink()
    div = Div()
    obj._link_props(div, ['text'], document, div)
    assert 'text' in div._callbacks
    cb = div._callbacks['text'][0]
    assert isinstance(cb, partial)
    assert cb.args == (document, div.ref['id'], None)
    assert cb.func == obj._server_change