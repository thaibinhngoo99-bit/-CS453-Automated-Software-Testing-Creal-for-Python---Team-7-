def sigmoidPrime(x):
    """ Derivative of logistic sigmoid. """
    tmp = sigmoid(x)
    return tmp * (1 - tmp)