def aRDwcalc(dat, datR, binspar, binsper, parmetric, permetric, rng, weights):
    print('Calculating anisotropic RD with weights...\n DR=')
    dr = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(range(len(datR))):
        ind = arbt.query_radius(datR[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([datR[i]], dat[j], parmetric)[0]
            dist1 = dist.cdist([datR[i]], dat[j], permetric)[0]
            dr += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=weights[j])[0]
    dr[dr == 0] = 1.0
    return dr / 2.0