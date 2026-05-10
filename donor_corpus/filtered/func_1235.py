def amulti_autocpr(datR, binspar, binsper, parmetric, permetric, rng, rweights, Nr, CORES=pcpus):
    RR = np.zeros((len(binspar) - 1, len(binsper) - 1))
    queues = [RetryQueue() for i in range(CORES)]
    args = [(datR, binspar, binsper, parmetric, permetric, rng, rweights, range(int(Nr * i / CORES), int(Nr * (i + 1) / CORES)), True, queues[i]) for i in range(CORES)]
    jobs = [Process(target=aRRwcalcp, args=a) for a in args]
    for j in jobs:
        j.start()
    for q in queues:
        RR += q.get()
    for j in jobs:
        j.join()
    RR[RR == 0] = 1.0
    print(RR)
    return RR