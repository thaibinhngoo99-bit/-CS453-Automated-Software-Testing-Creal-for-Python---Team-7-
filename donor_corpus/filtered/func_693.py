def initPopulation():
    population = np.random.rand(POPULATION_SIZE, calculatePolicySize())
    population = population * 2 - 1
    return population