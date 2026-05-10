def test_ensure_resource_is_added():
    app = App(__name__)
    app.add_resource('/404', resource=NoResource())
    first_key = next(iter(app.router.iter_rules()))
    endpoint = app.router._endpoints[first_key.endpoint]
    assert isinstance(endpoint, NoResource)
    debug = 1