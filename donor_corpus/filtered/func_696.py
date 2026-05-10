def evaluate(dnnmodel, population, gamesPlayed):
    scores = np.zeros(POPULATION_SIZE)
    for i in range(POPULATION_SIZE):
        nnFormatPolicyVector = applyPolicyVectorToNN(population[i])
        dnnmodel.set_weights(nnFormatPolicyVector)
        scores[i] = playGame(dnnmodel)
        gamesPlayed += 1
        writeCsv(3, gamesPlayed)
    return scores