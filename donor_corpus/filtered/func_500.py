def get_bad_scan_times():
    """Return list of Timestamps with bad scan times, from CSV data."""
    df = pd.read_csv('data-ggd/ggd_bad_scans.txt', comment='#')
    tstamps = pd.to_datetime(df['Timestamp']).to_list()
    return tstamps