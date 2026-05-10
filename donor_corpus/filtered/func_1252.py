def stddev(data):
    N = len(data)
    avg = sum(data) / N
    num = sum([(x - avg) ** 2 for x in data])
    den = N - 1
    stddev = (num / den) ** 0.5
    return stddev