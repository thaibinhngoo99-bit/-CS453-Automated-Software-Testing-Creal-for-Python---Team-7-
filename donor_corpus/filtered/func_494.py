def getEfficiency(cpnes, welfareMat):
    pneWelf = [welfareMat[cpne] for cpne in cpnes]
    opt = np.max(welfareMat)
    priceRatios = [float(pne) / opt for pne in pneWelf]
    return priceRatios