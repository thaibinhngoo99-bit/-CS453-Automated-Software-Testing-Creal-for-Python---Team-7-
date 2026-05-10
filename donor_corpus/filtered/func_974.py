def naive_schedule(_, outs, target):
    """Return the naive default schedule"""
    if 'gpu' in target.keys:
        raise RuntimeError('Cannot compile for GPU targets if no tuned schedule is found. Please see the warning messages above for more information about the failed workloads.')
    return te.create_schedule(outs[-1].op)