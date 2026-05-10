def test_reactive_html_templated_children():

    class TestTemplatedChildren(ReactiveHTML):
        children = param.List(default=[])
        _template = '\n        <select id="select">\n        {% for option in children %}\n        <option id="option-{{ loop.index0 }}">${children[{{ loop.index0 }}]}</option>\n        {% endfor %}\n        </div>\n        '
    assert TestTemplatedChildren._node_callbacks == {}
    assert TestTemplatedChildren._inline_callbacks == []
    assert TestTemplatedChildren._parser.children == {'option': 'children'}
    widget = TextInput()
    test = TestTemplatedChildren(children=[widget])
    root = test.get_root()
    assert test._attrs == {}
    assert root.looped == ['option']
    assert root.children == {'option': [widget._models[root.ref['id']][0]]}
    assert test._panes == {'children': [widget]}
    widget_new = TextInput()
    test.children = [widget_new]
    assert len(widget._models) == 0
    assert root.children == {'option': [widget_new._models[root.ref['id']][0]]}
    assert test._panes == {'children': [widget_new]}