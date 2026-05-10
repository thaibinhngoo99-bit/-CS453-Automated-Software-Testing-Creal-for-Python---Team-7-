def _dump_geometrycollection(obj, fmt):
    """
    Dump a GeoJSON-like GeometryCollection object to WKT.

    Input parameters and return value are the GEOMETRYCOLLECTION equivalent to
    :func:`_dump_point`.

    The WKT conversions for each geometry in the collection are delegated to
    their respective functions.
    """
    gc = 'GEOMETRYCOLLECTION (%s)'
    geoms = obj['geometries']
    geoms_wkt = []
    for geom in geoms:
        geom_type = geom['type']
        geoms_wkt.append(_dumps_registry.get(geom_type)(geom, fmt))
    gc %= ','.join(geoms_wkt)
    return gc