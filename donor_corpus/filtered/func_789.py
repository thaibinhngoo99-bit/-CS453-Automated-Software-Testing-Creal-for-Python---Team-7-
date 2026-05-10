def point_df_to_gdf(f, x_col='lon', y_col='lat', from_crs=WGS84):
    """
    Given a DataFrame of points with x coordinates
    in the column ``x_col`` and y coordinates in the column ``y_col``,
    with respect to the GeoPandas coordinate reference system
    ``from_crs`` (dictionary), convert the DataFrame into a GeoDataFrame
    with that coordinate reference system and with a ``'geometry'``
    column that corresponds to the points.
    Delete the original x and y columns, and return the result.
    """
    f = f.copy()
    f['geometry'] = f[[x_col, y_col]].apply(lambda p: sg.Point(p), axis=1)
    f = f.drop([x_col, y_col], axis=1)
    f = gpd.GeoDataFrame(f)
    f.crs = from_crs
    return f