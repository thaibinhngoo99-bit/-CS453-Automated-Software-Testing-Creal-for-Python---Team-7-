def match_and_filter(table, metadata, formula, min_sample_count, min_feature_count):
    """ Matches and aligns biom and metadata tables.

    This will also return the patsy representation.

    Parameters
    ----------
    table : biom.Table
        Table of abundances
    metadata : pd.DataFrame
        Sample metadata

    Returns
    -------
    table : biom.Table
        Filtered biom table
    metadata : pd.DataFrame
        Sample metadata
    """

    def sample_filter(val, id_, md):
        return id_ in metadata.index and np.sum(val) > min_sample_count

    def read_filter(val, id_, md):
        return np.sum(val > 0) > min_feature_count
    table = table.filter(sample_filter, axis='sample', inplace=False)
    table = table.filter(read_filter, axis='observation', inplace=False)
    metadata = metadata.loc[table.ids(axis='sample')]
    metadata = metadata.loc[~metadata.index.duplicated(keep='first')]

    def sort_f(xs):
        return [xs[metadata.index.get_loc(x)] for x in xs]
    table = table.sort(sort_f=sort_f, axis='sample')
    design = dmatrix(formula, metadata, return_type='dataframe')
    design = design.dropna()

    def design_filter(val, id_, md):
        return id_ in design.index
    table = table.filter(design_filter, axis='sample')
    return (table, metadata, design)