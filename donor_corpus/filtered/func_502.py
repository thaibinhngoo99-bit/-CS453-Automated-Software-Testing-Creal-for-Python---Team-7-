def _summary_to_scores(summary):
    """Convert summary from _read_log to scores dict and effective timestamp.

    Parameters:

    - summary: dict with int(pc4) -> [(query_time, appt_time), ...]

    Return:

    - scores dict: int(pc4) -> score (int or float or '?')
    - timestamp: middle query timestamp of this run.
    """
    scores = {k: '?' for k in PCODES}
    multi_pcs = {}
    for pc in PCODES:
        if isinstance(pc, tuple):
            for pc1 in pc:
                multi_pcs[pc1] = pc
    qtms = []
    dhm = _delta_time_hhmm
    for pc4, vlist in summary.items():
        pc4 = int(pc4)
        if pc4 not in scores:
            if pc4 in multi_pcs:
                pc4_key = multi_pcs[pc4]
            else:
                print(f'{pc4} not in list...')
                continue
        else:
            pc4_key = pc4
        if len(vlist) == 0:
            scores[pc4_key] = 7
            continue
        qtm = _mean_time([v[0] for v in vlist])
        qtms.append(qtm)
        atm = min((v[1] for v in vlist))
        qtm_00 = pd.Timestamp(qtm.strftime('%Y-%m-%dT00:00'))
        thresholds = [(3, qtm_00 + dhm('23:59')), (4, qtm + dhm('24:00')), (5, qtm_00 + dhm('48:00')), (6, qtm + dhm('48:00')), (6.3, qtm_00 + dhm('72:00')), (6.7, qtm + dhm('72:00')), (7, atm)]
        if qtm.hour < 9:
            thresholds.insert(0, (1, qtm_00 + dhm('13:00')))
        elif qtm.hour < 13:
            thresholds.insert(0, (1, qtm + dhm('4:00')))
        elif qtm.hour < 17:
            thresholds.insert(0, (1, qtm_00 + dhm('24:00')))
            thresholds.insert(1, (2, qtm + dhm('20:00')))
        else:
            thresholds.insert(0, (1, qtm_00 + dhm('24:00')))
            thresholds.insert(1, (2, qtm_00 + dhm('37:00')))
        for s, tm in thresholds:
            if atm < tm:
                scores[pc4_key] = s
                break
    if len(qtms) == 0:
        qtm_mid = pd.Timestamp(None)
    else:
        qtm_min = min(qtms)
        qtm_mid = qtm_min + (max(qtms) - qtm_min) / 2
    return (scores, qtm_mid)