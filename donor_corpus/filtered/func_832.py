def test_reactive_html_children():

    class TestChildren(ReactiveHTML):
        children = param.List(default=[])
        _template = '<div id="div">${children}</div>'
    assert TestChildren._node_callbacks == {}
    assert TestChildren._inline_callbacks == []
    assert TestChildren._parser.children == {'div': 'children'}
    widget = TextInput()
    test = TestChildren(children=[widget])
    root = test.get_root()
    assert test._attrs == {}
    assert root.children == {'div': [widget._models[root.ref['id']][0]]}
    assert len(widget._models) == 1
    assert test._panes == {'children': [widget]}
    widget_new = TextInput()
    test.children = [widget_new]
    assert len(widget._models) == 0
    assert root.children == {'div': [widget_new._models[root.ref['id']][0]]}
    assert test._panes == {'children': [widget_new]}
    test._cleanup(root)
    assert len(test._models) == 0
    assert len(widget_new._models) == 0