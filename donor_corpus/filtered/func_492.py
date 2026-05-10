def getPayoff(utilMap, listAcSet):

    def utilInd(index):
        jointAc = [listAcSet[j][ind] for j, ind in enumerate(index)]
        val = utilMap(jointAc)
        return val
    numPL = [len(pL) for pL in listAcSet]
    payoff = np.zeros(numPL)
    for ind in product(*[range(nI) for nI in numPL]):
        payoff[ind] = utilInd(ind)
    return payoff