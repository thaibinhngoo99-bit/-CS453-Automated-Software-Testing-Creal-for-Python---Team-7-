def aDDwcalc(dat, binspar, binsper, parmetric, permetric, rng, weights):
    print('Calculating anisotropic DD with weights...\n DD=')
    dd = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(range(len(dat))):
        ind = adbt.query_radius(dat[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([dat[i]], dat[j[j > i]], parmetric)[0]
            dist1 = dist.cdist([dat[i]], dat[j[j > i]], permetric)[0]
            dd += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper), weights=weights[j[j > i]])[0]
    dd[dd == 0] = 1.0
    return dd