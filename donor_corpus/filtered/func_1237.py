def amulti_crosscpr(dat, datR, binspar, binsper, parmetric, permetric, rng, rweights, Nd, CORES=pcpus):
    DR = np.zeros((len(binspar) - 1, len(binsper) - 1))
    queues = [RetryQueue() for i in range(CORES)]
    args = [(dat, datR, binspar, binsper, parmetric, permetric, rng, rweights, range(int(Nd * i / CORES), int(Nd * (i + 1) / CORES)), True, queues[i]) for i in range(CORES)]
    jobs = [Process(target=aDRwcalcp, args=a) for a in args]
    for j in jobs:
        j.start()
    for q in queues:
        DR += q.get()
    for j in jobs:
        j.join()
    DR[DR == 0] = 1.0
    print(DR / 2.0)
    return DR / 2.0