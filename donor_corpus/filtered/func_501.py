def _mean_time(ts_list):
    """Return mean timestamp value from list of timestamps."""
    ts0 = ts_list[0]
    delta_sum = pd.Timedelta(0)
    for ts in ts_list:
        delta_sum += ts - ts0
    ts_mean = ts0 + delta_sum / len(ts_list)
    return ts_mean