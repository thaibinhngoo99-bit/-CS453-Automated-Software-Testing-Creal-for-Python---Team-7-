def parallelize(func, list, size=None):
    if not size:
        size = len(list)
    if size <= 0:
        return None
    pool = Pool(size)
    result = pool.map(func, list)
    pool.close()
    pool.join()
    return result