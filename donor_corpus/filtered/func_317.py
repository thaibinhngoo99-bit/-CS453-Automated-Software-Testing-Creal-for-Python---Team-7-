def _load_polygon(tokens, string):
    """
    Has similar inputs and return value to to :func:`_load_point`, except is
    for handling POLYGON geometry.

    :returns:
        A GeoJSON `dict` Polygon representation of the WKT ``string``.
    """
    open_parens = (next(tokens), next(tokens))
    if not open_parens == ('(', '('):
        raise ValueError(INVALID_WKT_FMT % string)
    coords = []
    ring = []
    on_ring = True
    try:
        pt = []
        for t in tokens:
            if t == ')' and on_ring:
                ring.append(pt)
                coords.append(ring)
                on_ring = False
            elif t == ')' and (not on_ring):
                break
            elif t == '(':
                ring = []
                pt = []
                on_ring = True
            elif t == ',' and on_ring:
                ring.append(pt)
                pt = []
            elif t == ',' and (not on_ring):
                pass
            else:
                pt.append(float(t))
    except tokenize.TokenError:
        raise ValueError(INVALID_WKT_FMT % string)
    return dict(type='Polygon', coordinates=coords)