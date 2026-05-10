def test_reactive_html_basic():

    class Test(ReactiveHTML):
        int = param.Integer(default=3, doc='An integer')
        float = param.Number(default=3.14, doc='A float')
        _template = '<div id="div" width=${int}></div>'
    data_model = Test._data_model
    assert data_model.__name__ == 'Test1'
    properties = data_model.properties()
    assert 'int' in properties
    assert 'float' in properties
    int_prop = data_model.lookup('int')
    assert isinstance(int_prop.property, bp.Int)
    assert int_prop.class_default(data_model) == 3
    float_prop = data_model.lookup('float')
    assert isinstance(float_prop.property, bp.Float)
    assert float_prop.class_default(data_model) == 3.14
    assert Test._node_callbacks == {}
    test = Test()
    root = test.get_root()
    assert test._attrs == {'div': [('width', ['int'], '{int}')]}
    assert root.callbacks == {}
    assert root.events == {}