def amulti_autocp(dat, binspar, binsper, parmetric, permetric, rng, weights, Nd, CORES=pcpus):
    DD = np.zeros((len(binspar) - 1, len(binsper) - 1))
    queues = [RetryQueue() for i in range(CORES)]
    args = [(dat, binspar, binsper, parmetric, permetric, rng, weights, range(int(Nd * i / CORES), int(Nd * (i + 1) / CORES)), True, queues[i]) for i in range(CORES)]
    jobs = [Process(target=aDDwcalcp, args=a) for a in args]
    for j in jobs:
        j.start()
    for q in queues:
        DD += q.get()
    for j in jobs:
        j.join()
    DD[DD == 0] = 1.0
    print(DD)
    return DD