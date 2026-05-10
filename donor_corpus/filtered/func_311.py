def _dump_multipoint(obj, fmt):
    """
    Dump a GeoJSON-like MultiPoint object to WKT.

    Input parameters and return value are the MULTIPOINT equivalent to
    :func:`_dump_point`.
    """
    coords = obj['coordinates']
    mp = 'MULTIPOINT (%s)'
    points = (' '.join((fmt % c for c in pt)) for pt in coords)
    points = ('(%s)' % pt for pt in points)
    mp %= ', '.join(points)
    return mp