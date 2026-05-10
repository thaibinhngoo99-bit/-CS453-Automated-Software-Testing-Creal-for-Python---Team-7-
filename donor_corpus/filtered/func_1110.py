def merge_dicts(*dicts, **kwargs):
    """ Merge all dicts in `*dicts` into a single dict, and return the result. If any of the entries
        in `*dicts` is None, and `default` is specified as keyword argument, then return `default`. """
    result = {}
    for d in dicts:
        if d is None and 'default' in kwargs:
            return kwargs['default']
        if d:
            result.update(d)
    return result