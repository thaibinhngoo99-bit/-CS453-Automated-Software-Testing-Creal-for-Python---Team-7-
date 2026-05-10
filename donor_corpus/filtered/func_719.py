def test_ensure_a_classic_like_class_is_routed():
    app = App(__name__)

    @app.add('/trash')
    class GoodClass(object):

        def render(self, request):
            return b'Rendered'
    first_key = next(iter(app.router.iter_rules()))
    endpoint = app.router._endpoints[first_key.endpoint]
    assert isinstance(endpoint, ViewClassResource)
    debug = 1