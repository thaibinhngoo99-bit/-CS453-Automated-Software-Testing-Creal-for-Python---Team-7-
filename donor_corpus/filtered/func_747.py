def get_ops(base):
    """
    Returns an *Operations instance, depending on the base.

    Parameters
    ----------
    base : float, 'linear', 'e'
        The base for the Operations instance.

    """
    if base in cache:
        ops = cache[base]
    else:
        ops = LogOperations(base)
        cache[base] = ops
    return ops