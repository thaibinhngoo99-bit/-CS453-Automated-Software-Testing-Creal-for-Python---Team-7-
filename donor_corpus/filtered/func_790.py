def point_gdf_to_df(f, x_col='lon', y_col='lat', to_crs=WGS84):
    """
    The inverse of :func:`point_df_to_gdf`.
    Given a GeoDataFrame of points, convert to the coordinate reference
    system ``to_crs`` (dictionary), then split its ``'geometry'`` column
    into x coordinates in the column ``x_col`` and y coordinates in the
    columns ``y_col``, deleting the ``'geometry'`` column afterwards.
    Coerce the result into a DataFrame and return it.
    """
    f = f.copy()
    if f.crs is None:
        raise ValueError('GeoDataFrame needs a crs attribute')
    if f.crs != to_crs:
        f = f.to_crs(to_crs)
    f[x_col], f[y_col] = zip(*f['geometry'].map(lambda p: p.coords[0]))
    del f['geometry']
    return pd.DataFrame(f)