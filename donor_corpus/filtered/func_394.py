def sqrtm(M):
    """ Returns the symmetric semi-definite positive square root of a matrix. """
    r = real_if_close(expm2(0.5 * logm(M)), 1e-08)
    return (r + r.T) / 2