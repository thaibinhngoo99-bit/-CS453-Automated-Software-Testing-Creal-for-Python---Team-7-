def aRDwcalcp(dat, datR, binspar, binsper, parmetric, permetric, rng, weights, rNr, multi=False, queue=0):
    dr = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(rNr):
        ind = adbt.query_radius(datR[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([datR[i]], dat[j], parmetric)[0]
            dist1 = dist.cdist([datR[i]], dat[j], permetric)[0]
            dr += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=weights[j])[0]
    if multi:
        queue.put(dr)
    else:
        return dr
    return dr