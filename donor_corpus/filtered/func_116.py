def compare_exceptions(a, b):
    a, b = (get_compare_name(a), get_compare_name(b))
    ta = get_type(a)
    tb = get_type(b)
    if ta == None:
        raise Exception('Exception class not found %s ' % a)
    if tb == None:
        raise Exception('Exception class not found %s ' % b)
    if ta.IsSubclassOf(tb):
        return -1
    if tb.IsSubclassOf(ta):
        return 1
    da = exception_distance(ta)
    db = exception_distance(tb)
    if da != db:
        return db - da
    return cmp(ta.Name, tb.Name)