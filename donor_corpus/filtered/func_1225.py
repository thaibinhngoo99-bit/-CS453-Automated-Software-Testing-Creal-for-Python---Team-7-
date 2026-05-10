def aRDcalc(dat, datR, binspar, binsper, parmetric, permetric, rng):
    print('Calculating anisotropic RD...\n RD=')
    rd = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(range(len(datR))):
        ind = arbt.query_radius(datR[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([datR[i]], dat[j[j > i]], parmetric)[0]
            dist1 = dist.cdist([datR[i]], dat[j[j > i]], permetric)[0]
            rd += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper))[0]
    rd[rd == 0] = 1.0
    print(rd)
    return rd