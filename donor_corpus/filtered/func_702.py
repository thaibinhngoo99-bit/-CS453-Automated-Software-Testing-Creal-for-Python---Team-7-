def mutation(crossoverPopulation):
    i = int((POPULATION_SIZE - ELITE_SET_SIZE) * np.random.random_sample())
    j = int(calculatePolicySize() * np.random.random_sample())
    for _ in range(int(i * j * MUTATION_RATE)):
        crossoverPopulation[i][j] = np.random.random_sample() * 2 - 1
    return crossoverPopulation