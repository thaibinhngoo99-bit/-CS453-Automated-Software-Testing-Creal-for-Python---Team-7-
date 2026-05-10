def run_distance_matrix_job(client, origins_gdf, destinations_gdf, out_dir, origin_id_col=None, destination_id_col=None, max_elements=MAX_ELEMENTS, **distance_matrix_kwargs):
    """
    Compute the duration-distance matrix between the given origins
    and destinations.
    To do this, call the Google Maps Distance Matrix API repeatedly,
    ensuring that each call uses no more than ``max_elements`` elements.

    INPUT:

    - ``client``: google-maps-services-python Client instance
    - ``origins_gdf``: GeoDataFrame of points; the origins
    - ``destinations_gdf``: GeoDataFrame of points; the destinations
    - ``out_dir``: string or Path object of a directory at which
      to store the output files; create the directory if it does not
      exist
    - ``origin_id_col``: string; name of ID column in ``origins_gdf``
    - ``destination_id_col``: string; name of ID column in
      ``destinations_gdf``
    - ``max_elements``: integer; max number of elements allowable in
      one Google Maps Distance Matrix API call
    - ``distance_matrix_kwargs``: dictionary; keyword arguments for
      Google Maps Distance Matrix API

    OUTPUT:

    A collection of CSV files located at ``out_dir`` of the form output
    by :func:`to_df`, where the origins comes from ``origins_gdf`` and
    the destinations come from ``destinations_gdf``.
    Each file will contains one origin points and at most
    ``max_elements`` destination points, for a total of at most
    ``max_elements`` rows.
    An empty DataFrame with the expected column names will be saved to
    file if an HTTPError on Timeout exception occurs.
    This can happen if, for example, the daily query limit is exceeded.
    """
    o_gdf = origins_gdf.copy()
    d_gdf = destinations_gdf.copy()
    n_o = o_gdf.shape[0]
    n_d = d_gdf.shape[0]
    if origin_id_col is None:
        origin_id_col = 'ersatz_origin_id'
        o_gdf[origin_id_col] = make_ids(n_o, 'orig_row_')
    if destination_id_col is None:
        destination_id_col = 'ersatz_destination_id'
        d_gdf[destination_id_col] = make_ids(n_d, 'dest_row_')
    mode = distance_matrix_kwargs.get('mode', 'driving')
    out_dir = Path(out_dir)
    if not out_dir.exists():
        out_dir.mkdir(parents=True)
    for ix, orig_id in o_gdf[[origin_id_col]].itertuples():
        logger.info('Working on origin {} of {} (id {})'.format(ix + 1, n_o, orig_id))
        for j in range(math.ceil(n_d / max_elements)):
            n1 = max_elements * j
            n2 = min(max_elements * (j + 1), n_d)
            dest_id1, dest_id2 = (d_gdf[destination_id_col].iat[n1], d_gdf[destination_id_col].iat[n2 - 1])
            path = Path(out_dir) / '{}_from_{}_to_{}--{}.csv'.format(mode, orig_id, dest_id1, dest_id2)
            f = build_distance_matrix_df(client, o_gdf.loc[ix:ix], d_gdf.iloc[n1:n2], origin_id_col=origin_id_col, destination_id_col=destination_id_col, **distance_matrix_kwargs)
            f.to_csv(path, index=False)
            if f.empty:
                logger.info('* Failed to get data for ' + path.stem)