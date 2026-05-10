def test_reactive_html_templated_dict_children():

    class TestTemplatedChildren(ReactiveHTML):
        children = param.Dict(default={})
        _template = '\n        <select id="select">\n        {% for key, option in children.items() %}\n        <option id="option-{{ loop.index0 }}">${children[{{ key }}]}</option>\n        {% endfor %}\n        </div>\n        '
    assert TestTemplatedChildren._node_callbacks == {}
    assert TestTemplatedChildren._inline_callbacks == []
    assert TestTemplatedChildren._parser.children == {'option': 'children'}
    widget = TextInput()
    test = TestTemplatedChildren(children={'test': widget})
    root = test.get_root()
    assert test._attrs == {}
    assert root.looped == ['option']
    assert root.children == {'option': [widget._models[root.ref['id']][0]]}
    assert test._panes == {'children': [widget]}
    widget_model = widget._models[root.ref['id']][0]
    widget_new = TextInput()
    test.children = {'test': widget_new, 'test2': widget}
    assert len(widget._models) == 1
    assert root.children == {'option': [widget_new._models[root.ref['id']][0], widget_model]}
    assert test._panes == {'children': [widget_new, widget]}