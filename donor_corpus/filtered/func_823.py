def test_link():
    """Link two Reactive objects"""

    class ReactiveLink(Reactive):
        a = param.Parameter()
    obj = ReactiveLink()
    obj2 = ReactiveLink()
    obj.link(obj2, a='a')
    obj.a = 1
    assert obj.a == 1
    assert obj2.a == 1