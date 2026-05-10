def aRRwcalcp(datR, binspar, binsper, parmetric, permetric, rng, rweights, rNr, multi=False, queue=0):
    rr = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(rNr):
        ind = arbt.query_radius(datR[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([datR[i]], datR[j[j > i]], parmetric)[0]
            dist1 = dist.cdist([datR[i]], datR[j[j > i]], permetric)[0]
            rr += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=rweights[j[j > i]])[0]
    if multi:
        queue.put(rr)
    else:
        return rr
    return rr