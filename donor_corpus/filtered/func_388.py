def expln(x):
    """ This continuous function ensures that the values of the array are always positive.
        It is ln(x+1)+1 for x >= 0 and exp(x) for x < 0. """

    def f(val):
        if val < 0:
            return exp(val)
        else:
            return log(val + 1.0) + 1
    try:
        result = array(map(f, x))
    except TypeError:
        result = array(f(x))
    return result