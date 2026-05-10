def bruteFindNash(payoffList):
    TOLERANCE = 1e-07
    cpnes = list(np.argwhere(payoffList[0] > np.amax(payoffList[0], 0) - TOLERANCE))
    cpnes = [tuple(cpne) for cpne in cpnes]
    N = len(payoffList)
    for i in range(1, N):
        pMat = payoffList[i]
        for cpne in cpnes[:]:
            ind = cpne[:i] + (slice(None),) + cpne[i + 1:]
            if pMat[cpne] < np.max(pMat[ind]) - TOLERANCE:
                cpnes.pop(cpnes.index(cpne))
    return cpnes