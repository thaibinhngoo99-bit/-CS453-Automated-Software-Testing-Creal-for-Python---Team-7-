def aRRcalc(datR, binspar, binsper, parmetric, permetric, rng):
    print('Calculating anisotropic RR...\n RR=')
    rr = np.zeros((len(binspar) - 1, len(binsper) - 1))
    for i in tqdm(range(len(datR))):
        ind = arbt.query_radius(datR[i].reshape(1, -1), maxrad)
        for j in ind:
            dist0 = dist.cdist([datR[i]], datR[j[j > i]], parmetric)[0]
            dist1 = dist.cdist([datR[i]], datR[j[j > i]], permetric)[0]
            rr += np.histogram2d(dist0, dist1, range=rng, bins=(binspar, binsper))[0]
    rr[rr == 0] = 1.0
    print(rr)
    return rr