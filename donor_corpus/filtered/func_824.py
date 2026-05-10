def test_param_rename():
    """Test that Reactive renames params and properties"""

    class ReactiveRename(Reactive):
        a = param.Parameter()
        _rename = {'a': 'b'}
    obj = ReactiveRename()
    params = obj._process_property_change({'b': 1})
    assert params == {'a': 1}
    properties = obj._process_param_change({'a': 1})
    assert properties == {'b': 1}