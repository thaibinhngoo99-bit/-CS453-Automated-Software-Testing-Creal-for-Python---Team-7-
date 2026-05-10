def _dump_multipolygon(obj, fmt):
    """
    Dump a GeoJSON-like MultiPolygon object to WKT.

    Input parameters and return value are the MULTIPOLYGON equivalent to
    :func:`_dump_point`.
    """
    coords = obj['coordinates']
    mp = 'MULTIPOLYGON (%s)'
    polys = ', '.join(('(%s)' % ', '.join(('(%s)' % ', '.join((' '.join((fmt % c for c in pt)) for pt in ring)) for ring in poly)) for poly in coords))
    mp %= polys
    return mp