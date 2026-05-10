def get_scan_scores(df, tm_range):
    """Get scan scores as pc4 -> score dict.

    Parameters:

    - df: DataFrame with scan_time, req_date, req_pc4, opt0_short_addr,
      opt0_time, opt0_loc_id, etc.
    - tm_range: (tm_start, tm_stop) timestamps.

    Return:

    - tstamp: timestamp of the scan (mid-point)
    - scores: dict of pc4->score
    - min_wait: Timedelta of minimum wait time from scan to appointment
    """
    mask = (df['scan_time'] >= tm_range[0]) & (df['scan_time'] < tm_range[1])
    df1 = df.loc[mask]
    summary = {}
    for pc4, city_re in PCODES.items():
        pc4_tup = (pc4,) if isinstance(pc4, int) else pc4
        options = []
        req_pc4 = None
        for _, row in df1.loc[df1['req_pc4'].isin(pc4_tup)].iterrows():
            req_pc4 = int(row['req_pc4'])
            for i in range(3):
                addr = row[f'opt{i}_short_addr']
                if addr and re.match(f'{city_re}$', addr[5:]):
                    options.append((row['scan_time'], row[f'opt{i}_time']))
        if req_pc4 is not None:
            summary[req_pc4] = options
    scores, tstamp = _summary_to_scores(summary)
    if pd.isna(tstamp):
        tstamp = df1.iloc[len(df1) // 2]['scan_time']
    minwait, medwait = _get_min_wait(summary)
    if medwait == 999:
        medwait = pd.Timedelta(None)
    return (tstamp, scores, minwait, medwait)