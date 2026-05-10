def test_index(tl, hook):
    with HTTMock(customsforge), Index(tl=tl).executest(hook):
        hook.assert_success('CDLCs indexed')
    tl.set_use_elastic(False)
    with HTTMock(customsforge), Index(tl=tl).executest(hook):
        hook.assert_failure('CDLCs could not be indexed')