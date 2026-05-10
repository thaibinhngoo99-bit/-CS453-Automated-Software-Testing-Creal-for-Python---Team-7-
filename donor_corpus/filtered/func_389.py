def explnPrime(x):
    """ This function is the first derivative of the expln function (above).
        It is needed for the backward pass of the module. """

    def f(val):
        if val < 0:
            return exp(val)
        else:
            return 1.0 / (val + 1.0)
    try:
        result = array(map(f, x))
    except TypeError:
        result = array(f(x))
    return result