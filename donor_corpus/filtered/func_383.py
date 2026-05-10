def semilinear(x):
    """ This function ensures that the values of the array are always positive. It is
        x+1 for x=>0 and exp(x) for x<0. """
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
            return val + 1.0
    return array(map(f, x)).reshape(shape)