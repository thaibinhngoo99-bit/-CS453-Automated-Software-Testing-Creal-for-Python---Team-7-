def selection(scores, population):
    eliteSet = np.zeros((ELITE_SET_SIZE, calculatePolicySize()))
    scoresTemp = np.copy(scores)
    for i in range(ELITE_SET_SIZE):
        index = np.argmax(scoresTemp)
        scoresTemp[index] = 0
        eliteSet[i] = population[index]
    return eliteSet