def pd_colupdate(dataframe: pd.DataFrame, coldict: dict) -> pd.DataFrame:
    """
    Rename and filter Pandas Dataframe columns using python dictionary.

    Column names provided in coldict follow the same format as expected by
    pd.DataFrame.rename(columns=dict). For example: {"current":"new", "current2":"new2"}

    Columns in returned dataframe are filtered by those provided to be renamed.

    Returns a modified pd.Dataframe copy
    """
    logger.info('Renaming and filtering dataframe columns using coldict key:values.')
    dataframe = dataframe.rename(columns=coldict)
    dataframe = dataframe[[val for key, val in coldict.items()]].copy()
    return dataframe