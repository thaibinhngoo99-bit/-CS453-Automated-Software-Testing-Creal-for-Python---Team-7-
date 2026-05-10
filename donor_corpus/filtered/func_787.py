def make_ids(n, prefix='row_'):
    """
    Return a list of ``n`` (integer) unique strings of the form
    ``prefix``<number>.
    """
    k = int(math.log10(n)) + 1
    return [prefix + '{num:0{pad}d}'.format(num=i, pad=k) for i in range(n)]