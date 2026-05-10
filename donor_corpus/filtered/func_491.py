def getPolList(states, acSet):
    numStates = len(states)
    numActions = len(acSet)
    detPol = getAllDetPol(numStates, numActions)
    return [Policy(states, pol, acSet) for pol in detPol]