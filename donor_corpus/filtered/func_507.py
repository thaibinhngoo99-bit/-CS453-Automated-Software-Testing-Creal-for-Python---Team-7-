def get_scan_scores_df(df, tm_ranges, decimal_comma=True):
    """Get scan scores as dataframe, from csv dataframe.

    Blacklisted scan times are dropped.

    Parameters:

    - df: DataFrame with scan_time, req_date, req_pc4, opt0_short_addr,
      opt0_time, opt0_loc_id, etc.
    - tm_ranges: list of timestamps (+one at the end) with boundaries
      of timestamp ranges.
    - decimal_comma: True to have string values 6,3 rather than float 6.3.

    Return:

    - Dataframe with scores, date_str, time_str, pc4, min_wait, med_wait as columns.
    """
    n = len(tm_ranges)
    records = []
    index = []
    minwait_hs = []
    medwait_hs = []
    bad_stimes = get_bad_scan_times()
    for i in range(n - 1):
        tm_ra = tm_ranges[i:i + 2]
        is_ok = True
        for tm in bad_stimes:
            if tm_ra[0] <= tm < tm_ra[1]:
                is_ok = False
                break
        if not is_ok:
            print(f'Dropped scan at {tm_ra[0].strftime('%Y-%m-%d %H:%M')}')
            continue
        tm, scores, minwait, medwait = get_scan_scores(df, tm_ra)
        records.append(scores)
        index.append(tm)
        minwait_hs.append(minwait.total_seconds() / 3600)
        medwait_hs.append(medwait.total_seconds() / 3600)
    dates = [t.strftime('%Y-%m-%d') for t in index]
    times = [t.strftime('%H:%M') for t in index]
    sdf = pd.DataFrame.from_records(records)
    sdf.insert(0, 'Time', times)
    sdf.insert(0, 'Date', dates)
    sdf['min_wait_h'] = np.around(minwait_hs, 2)
    sdf['med_wait_h'] = np.around(medwait_hs, 2)
    sdf.loc[sdf['min_wait_h'].isna(), 'min_wait_h'] = 999
    sdf.columns = ['/'.join([str(x) for x in c]) if isinstance(c, tuple) else c for c in sdf.columns]
    if decimal_comma:
        for c in sdf.columns[2:]:
            sdf[c] = sdf[c].astype(str)
            sdf[c] = sdf[c].str.replace('.', ',', regex=False)
            sdf[c] = sdf[c].str.replace(',0$', '', regex=False)
            sdf[c] = sdf[c].str.replace('?', '', regex=False)
    return sdf