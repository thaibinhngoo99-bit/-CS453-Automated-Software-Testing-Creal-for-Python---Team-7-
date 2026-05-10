def _get_min_wait(summary):
    """Return minimum and median wait Timedelta between scan time and appointment.

    summary is dict of pc4 -> list of timestamps
    No data -> 999 h.

    For the median, NaT is counted as infinite.
    """
    wtimes = []
    for _, vlist in summary.items():
        wtimes_this = [atm - qtm for qtm, atm in vlist]
        wtimes.append(min(wtimes_this) if wtimes_this else pd.Timedelta(99, 'h'))
    minwait = min(wtimes) if wtimes else 999
    medwait = pd.Timedelta(np.median(wtimes))
    return (minwait, medwait)