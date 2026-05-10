def _dump_multilinestring(obj, fmt):
    """
    Dump a GeoJSON-like MultiLineString object to WKT.

    Input parameters and return value are the MULTILINESTRING equivalent to
    :func:`_dump_point`.
    """
    coords = obj['coordinates']
    mlls = 'MULTILINESTRING (%s)'
    linestrs = ('(%s)' % ', '.join((' '.join((fmt % c for c in pt)) for pt in linestr)) for linestr in coords)
    mlls %= ', '.join((ls for ls in linestrs))
    return mlls