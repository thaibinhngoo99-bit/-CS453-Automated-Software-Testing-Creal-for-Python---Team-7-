def aDDcalc(dat, binspar, binsper, parmetric, permetric, rng):
    print('Calculating anisotropic DD...\n DD=')
    dd = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(range(len(dat))):
        ind = adbt.query_radius(dat[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([dat[i]], dat[j[j > i]], parmetric)[0]
            dist1 = dist.cdist([dat[i]], dat[j[j > i]], permetric)[0]
            dd += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper))[0]
    dd[dd == 0] = 1.0
    print(dd)
    return dd