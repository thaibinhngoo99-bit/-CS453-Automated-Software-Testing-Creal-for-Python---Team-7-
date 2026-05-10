def crossover(scores, population):
    crossoverSet = np.zeros((POPULATION_SIZE, calculatePolicySize()))
    selectionProbability = np.array(scores) / np.sum(scores)
    for i in range(POPULATION_SIZE - ELITE_SET_SIZE):
        randomIndex = np.random.choice(range(POPULATION_SIZE), p=selectionProbability)
        policy1 = population[randomIndex]
        randomIndex = np.random.choice(range(POPULATION_SIZE), p=selectionProbability)
        policy2 = population[randomIndex]
        newPolicy = cross(policy1, policy2)
        crossoverSet[i] = newPolicy
    return crossoverSet