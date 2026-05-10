def aDRwcalcp(dat, datR, binspar, binsper, parmetric, permetric, rng, rweights, rNd, multi=False, queue=0):
    dr = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(rNd):
        ind = arbt.query_radius(dat[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([dat[i]], datR[j], parmetric)[0]
            dist1 = dist.cdist([dat[i]], datR[j], permetric)[0]
            dr += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=rweights[j])[0]
    if multi:
        queue.put(dr)
    else:
        return dr
    return dr