def aDDwcalcp(dat, binspar, binsper, parmetric, permetric, rng, weights, rNd, multi=False, queue=0):
    dd = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(rNd):
        ind = adbt.query_radius(dat[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([dat[i]], dat[j[j > i]], parmetric)[0]
            dist1 = dist.cdist([dat[i]], dat[j[j > i]], permetric)[0]
            dd += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=weights[j[j > i]])[0]
    if multi:
        queue.put(dd)
    else:
        return dd
    return dd