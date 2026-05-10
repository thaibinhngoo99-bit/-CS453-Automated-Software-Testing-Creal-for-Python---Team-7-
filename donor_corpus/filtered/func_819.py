def read_metadata(filepath):
    """ Reads in a sample metadata file

    Parameters
    ----------
    filepath: str
       The file path location of the sample metadata file

    Returns
    -------
    pd.DataFrame :
       The metadata table with inferred types.
    """
    metadata = pd.read_table(filepath, dtype=object)
    cols = metadata.columns
    metadata = metadata.set_index(cols[0])
    metadata = _type_cast_to_float(metadata.copy())
    return metadata