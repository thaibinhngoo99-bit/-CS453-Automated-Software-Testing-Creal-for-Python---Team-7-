def load_multi_csvs(csv_fnames):
    """Return DataFrame and list of start times (+1)"""
    dfs = []
    start_tms = []
    for f in csv_fnames:
        df, st = load_csv(f)
        dfs.append(df)
        start_tms.extend(st[:-1])
    df = pd.concat(dfs).reset_index()
    start_tms.append(df.iloc[-1]['scan_time'] + pd.Timedelta('1 min'))
    return (df, start_tms)