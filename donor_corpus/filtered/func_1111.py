def recurse_object(obj, func, path=''):
    """ Recursively apply `func` to `obj` (may be a list, dict, or other object). """
    obj = func(obj, path=path)
    if isinstance(obj, list):
        for i in range(len(obj)):
            tmp_path = '%s[%s]' % (path or '.', i)
            obj[i] = recurse_object(obj[i], func, tmp_path)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            tmp_path = '%s%s' % (path + '.' if path else '', k)
            obj[k] = recurse_object(v, func, tmp_path)
    return obj