def pd_export(dataframe: pd.DataFrame, export_type: str, df_name: str, temp_name: bool=False, df_name_prefix: str='', df_name_suffix: str='', dir_name: str='.', config_box: Box=None, index=True, header=True) -> str:
    """
    Exports dataframe to file formats using various options

    Return a filepaths for the exported Dataframe
    """
    if temp_name and dir_name != '':
        filepath = mkstemp(suffix=df_name_suffix, prefix=df_name_prefix, dir=dir_name)[1]
    elif config_box and dir_name == '':
        filepath = os.path.join(config_box.extracttempdir, f'{df_name_prefix}{df_name}{df_name_suffix}.{export_type}')
    else:
        filename = f'{df_name_prefix}{df_name}{df_name_suffix}.{export_type}'
        filepath = os.path.join(dir_name, filename)
    logger.info('Creating %s file %s from dataframe.', export_type, filepath)
    if export_type == 'parquet':
        dataframe.to_parquet(path=filepath, index=index)
    elif export_type == 'csv':
        dataframe.to_csv(filepath, index=index, header=header)
    return filepath