def test_type_field_resolver_resolves_unknown_kind():

    class Unk(object):
        pass
    with raises(ValueError) as excinfo:
        TypeFieldResolvers.kind(Unk())
    assert 'Unknown kind of type: ' in str(excinfo.value)