def approxChiFunction(dim):
    """ Returns Chi (expectation of the length of a normal random vector)
    approximation according to: Ostermeier 1997. """
    dim = float(dim)
    return sqrt(dim) * (1 - 1 / (4 * dim) + 1 / (21 * dim ** 2))