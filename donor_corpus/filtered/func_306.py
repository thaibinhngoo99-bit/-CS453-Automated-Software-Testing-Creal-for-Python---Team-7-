def loads(string):
    """
    Construct a GeoJSON `dict` from WKT (`string`).
    """
    sio = StringIO.StringIO(string)
    tokens = (x[1] for x in tokenize.generate_tokens(sio.readline))
    tokens = _tokenize_wkt(tokens)
    geom_type = next(tokens)
    importer = _loads_registry.get(geom_type)
    if importer is None:
        _unsupported_geom_type(geom_type)
    return importer(tokens, string)