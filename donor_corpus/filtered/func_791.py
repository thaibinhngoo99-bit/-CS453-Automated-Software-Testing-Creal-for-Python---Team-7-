def build_distance_matrix_df(client, origins_gdf, destinations_gdf, origin_id_col=None, destination_id_col=None, max_elements=MAX_ELEMENTS, **distance_matrix_kwargs):
    """
    Compute the duration-distance matrix between the given origins
    and destinations, assuming that the number of origins multiplied
    by the number of destinations is at most ``max_elements``.
    To do this, call the Google Maps Distance Matrix API once.

    INPUT:

    - ``client``: google-maps-services-python Client instance
    - ``origins_gdf``: GeoDataFrame of point; the origins
    - ``destinations_gdf``: GeoDataFrame of points; the destinations
    - ``origin_id_col``: string; name of ID column in ``origins_gdf``
    - ``destination_id_col``: string; name of ID column in
      ``destinations_gdf``
    - ``max_elements``: integer; max number of elements allowable in
      one Google Maps Distance Matrix API call
    - ``distance_matrix_kwargs``: dictionary; keyword arguments for
      Google Maps Distance Matrix API

    OUTPUT:

    A DataFrame of the form output by :func:`to_df` where the origins
    come from ``origins_gdf`` and the destinations come from
    ``destinations_gdf``.

    Return an empty DataFrame with the expected column names if an
    HTTPError on Timeout exception occurs.
    """
    o_gdf = origins_gdf.copy()
    d_gdf = destinations_gdf.copy()
    n = o_gdf.shape[0] * d_gdf.shape[0]
    if n > max_elements:
        raise ValueError('Number of origins times number of destinations is {}, which exceeds threshold of {} elements'.format(n, max_elements))
    if o_gdf.crs != WGS84:
        o_gdf = o_gdf.to_crs(WGS84)
    if origin_id_col is None:
        origin_id_col = 'temp_id'
        o_gdf[origin_id_col] = make_ids(o_gdf.shape[0])
    o_locs = [geo.coords[0] for geo in o_gdf['geometry']]
    o_ids = o_gdf[origin_id_col].values
    if d_gdf.crs != WGS84:
        d_gdf = d_gdf.to_crs(WGS84)
    if destination_id_col is None:
        destination_id_col = 'temp_id'
        d_gdf[destination_id_col] = make_ids(d_gdf.shape[0])
    d_locs = [geo.coords[0] for geo in d_gdf['geometry']]
    d_ids = d_gdf[destination_id_col].values
    try:
        r = client.distance_matrix(flip_coords(o_locs), flip_coords(d_locs), **distance_matrix_kwargs)
        f = to_df(r, o_ids, d_ids)
    except (googlemaps.exceptions.HTTPError, googlemaps.exceptions.Timeout):
        f = pd.DataFrame(columns=['origin_address', 'origin_id', 'destination_address', 'destination_id', 'duration', 'distance'])
    return f