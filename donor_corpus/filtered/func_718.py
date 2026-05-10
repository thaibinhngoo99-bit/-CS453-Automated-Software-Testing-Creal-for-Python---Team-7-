def test_ensure_blows_up_with_a_bad_add():
    app = App(__name__)
    bad_asset = sentinel
    with pytest.raises(ValueError) as excinfo:
        app.add('/trash')(bad_asset)
        assert 'expected callable|Object|twisted.web.resource.Resource' in str(excinfo.value)