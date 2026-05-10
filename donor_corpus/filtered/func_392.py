def multivariateCauchy(mu, sigma, onlyDiagonal=True):
    """ Generates a sample according to a given multivariate Cauchy distribution. """
    if not onlyDiagonal:
        u, s, d = svd(sigma)
        coeffs = sqrt(s)
    else:
        coeffs = diag(sigma)
    r = rand(len(mu))
    res = coeffs * tan(pi * (r - 0.5))
    if not onlyDiagonal:
        res = dot(d, dot(res, u))
    return res + mu