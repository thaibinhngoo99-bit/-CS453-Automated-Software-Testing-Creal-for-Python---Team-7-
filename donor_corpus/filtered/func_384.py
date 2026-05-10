def semilinearPrime(x):
    """ This function is the first derivative of the semilinear function (above).
        It is needed for the backward pass of the module. """
    try:
        shape = x.shape
        x.flatten()
        x = x.tolist()
    except AttributeError:
        shape = (1, len(x))

    def f(val):
        if val < 0:
            return safeExp(val)
        else:
            return 1.0
    return array(map(f, x)).reshape(shape)