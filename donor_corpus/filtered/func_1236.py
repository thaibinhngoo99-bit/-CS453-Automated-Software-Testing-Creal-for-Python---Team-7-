def amulti_crosscp(dat, datR, binspar, binsper, parmetric, permetric, rng, weights, Nr, CORES=pcpus):
    RD = np.zeros((len(binspar) - 1, len(binsper) - 1))
    queues = [RetryQueue() for i in range(CORES)]
    args = [(dat, datR, binspar, binsper, parmetric, permetric, rng, weights, range(int(Nr * i / CORES), int(Nr * (i + 1) / CORES)), True, queues[i]) for i in range(CORES)]
    jobs = [Process(target=aRDwcalcp, args=a) for a in args]
    for j in jobs:
        j.start()
    for q in queues:
        RD += q.get()
    for j in jobs:
        j.join()
    RD[RD == 0] = 1.0
    print(RD / 2.0)
    return RD / 2.0