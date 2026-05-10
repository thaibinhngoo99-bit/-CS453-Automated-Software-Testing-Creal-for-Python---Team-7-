def _load_multipolygon(tokens, string):
    """
    Has similar inputs and return value to to :func:`_load_point`, except is
    for handling MULTIPOLYGON geometry.

    :returns:
        A GeoJSON `dict` MultiPolygon representation of the WKT ``string``.
    """
    open_paren = next(tokens)
    if not open_paren == '(':
        raise ValueError(INVALID_WKT_FMT % string)
    polygons = []
    while True:
        try:
            poly = _load_polygon(tokens, string)
            polygons.append(poly['coordinates'])
            t = next(tokens)
            if t == ')':
                break
        except StopIteration:
            raise ValueError(INVALID_WKT_FMT % string)
    return dict(type='MultiPolygon', coordinates=polygons)