def test_reactive_html_templated_children_add_loop_id():

    class TestTemplatedChildren(ReactiveHTML):
        children = param.List(default=[])
        _template = '\n        <select id="select">\n        {%- for option in children %}\n          <option id="option">${children[{{ loop.index0 }}]}</option>\n        {%- endfor %}\n        </select>\n        '
    assert TestTemplatedChildren._node_callbacks == {}
    assert TestTemplatedChildren._inline_callbacks == []
    assert TestTemplatedChildren._parser.children == {'option': 'children'}
    test = TestTemplatedChildren(children=['A', 'B', 'C'])
    assert test._get_template()[0] == '\n        <select id="select-${id}">\n          <option id="option-0-${id}"></option>\n          <option id="option-1-${id}"></option>\n          <option id="option-2-${id}"></option>\n        </select>\n        '
    model = test.get_root()
    assert test._attrs == {}
    assert model.looped == ['option']