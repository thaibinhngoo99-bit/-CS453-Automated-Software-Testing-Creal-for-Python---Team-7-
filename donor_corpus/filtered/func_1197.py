def _add_logging(dsk, ignore=None):
    """
    Add logging to a Dask graph.

    @param dsk: The Dask graph.

    @return: New Dask graph.
    """
    ctx = current_action()
    result = {}
    keys = toposort(dsk)

    def simplify(k):
        if isinstance(k, str):
            return k
        return '-'.join((str(o) for o in k))
    key_names = {}
    for key in keys:
        value = dsk[key]
        if not callable(value) and value in keys:
            key_names[key] = key_names[value]
        else:
            key_names[key] = simplify(key)
    key_to_action_id = {key: str(ctx.serialize_task_id(), 'utf-8') for key in keys}
    for key in keys:
        func = dsk[key][0]
        args = dsk[key][1:]
        if not callable(func):
            result[key] = dsk[key]
            continue
        wrapped_func = _RunWithEliotContext(task_id=key_to_action_id[key], func=func, key=key_names[key], dependencies=[key_names[k] for k in get_dependencies(dsk, key)])
        result[key] = (wrapped_func,) + tuple(args)
    assert result.keys() == dsk.keys()
    return result