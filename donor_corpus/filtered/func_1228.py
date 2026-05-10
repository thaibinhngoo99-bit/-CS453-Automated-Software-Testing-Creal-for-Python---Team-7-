def aDRwcalc(dat, datR, binspar, binsper, parmetric, permetric, rng, rweights):
    print('Calculating anisotropic DR with weights...\n DR=')
    dr = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(range(len(dat))):
        ind = arbt.query_radius(dat[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([dat[i]], datR[j], parmetric)[0]
            dist1 = dist.cdist([dat[i]], datR[j], permetric)[0]
            dr += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=rweights[j])[0]
    dr[dr == 0] = 1.0
    return dr / 2.0