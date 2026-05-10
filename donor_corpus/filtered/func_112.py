def collect_excs():
    ret = []
    for e in exceptions.__dict__.values():
        if not hasattr(e, '__bases__'):
            continue
        if e.__name__ == 'exceptions':
            continue
        if e.__name__ == '__builtin__':
            continue
        assert len(e.__bases__) <= 1, e
        if len(e.__bases__) == 0:
            continue
        else:
            supername = e.__bases__[0].__name__
        ret.append((e, supername))
    return ret