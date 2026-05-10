def compute_cost(n, cost=0.5 / 1000, num_freebies=0, daily_limit=100000, chunk_size=MAX_ELEMENTS):
    """
    Estimate the cost of a sequence of Google Maps Distance Matrix
    queries comprising a total of n elements at ``cost`` USD per
    element, where the first ``num_freebies`` (integer) elements are
    free.
    Return a Series that includes the cost and some other metadata.
    """
    d = OrderedDict()
    d['#elements'] = n
    d['exceeds {!s}-element daily limit?'.format(daily_limit)] = n > daily_limit
    d['estimated cost for job in USD'] = max(0, n - num_freebies) * cost
    d['estimated duration for job in minutes'] = n / chunk_size / 60
    return pd.Series(d)