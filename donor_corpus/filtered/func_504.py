def load_csv(csv_fname):
    """Return DataFrame and list of start times (+1)."""
    df = pd.read_csv(csv_fname, comment='#')
    df['req_pc4'] = df['req_pc4'].astype(int)
    for c in df.columns:
        if c.endswith('_time') or c.endswith('_date'):
            df[c] = pd.to_datetime(df[c])
        else:
            df.loc[df[c].isna(), c] = None
    start_tms = df.loc[df['scan_time'].diff() > pd.Timedelta('10 min'), 'scan_time']
    start_tms = [df.iloc[0]['scan_time']] + list(start_tms)
    start_tms += [df.iloc[-1]['scan_time'] + pd.Timedelta('1 min')]
    return (df, start_tms)