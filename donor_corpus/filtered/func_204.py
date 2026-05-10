def _parse_table(json_info):
    df = pd.DataFrame(json_info)
    if df.empty:
        return df
    del df['maxAge']
    df.set_index('endDate', inplace=True)
    df.index = pd.to_datetime(df.index, unit='s')
    df = df.transpose()
    df.index.name = 'Breakdown'
    return df