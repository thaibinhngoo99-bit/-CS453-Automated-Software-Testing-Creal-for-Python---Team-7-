def tanhPrime(x):
    """ Derivative of tanh. """
    tmp = tanh(x)
    return 1 - tmp * tmp