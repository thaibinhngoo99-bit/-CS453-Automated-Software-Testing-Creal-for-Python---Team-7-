def generateNewGeneration(scores, population):
    elitePopulation = selection(scores, population)
    crossoverPopulation = crossover(scores, population)
    mutationPopulation = mutation(crossoverPopulation)
    for i in range(ELITE_SET_SIZE):
        mutationPopulation[POPULATION_SIZE - ELITE_SET_SIZE + i] = elitePopulation[i]
    return mutationPopulation