def dumps(obj, decimals=16):
    """
    Dump a GeoJSON-like `dict` to a WKT string.
    """
    geom_type = obj['type']
    exporter = _dumps_registry.get(geom_type)
    if exporter is None:
        _unsupported_geom_type(geom_type)
    fmt = '%%.%df' % decimals
    return exporter(obj, fmt)