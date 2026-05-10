def loadPolicy(filename, population, index):
    policy = np.load(filename)
    print('Loaded\n', policy)
    population[index] = policy