def multivariateNormalPdf(z, x, sigma):
    """ The pdf of a multivariate normal distribution (not in scipy).
    The sample z and the mean x should be 1-dim-arrays, and sigma a square 2-dim-array. """
    assert len(z.shape) == 1 and len(x.shape) == 1 and (len(x) == len(z)) and (sigma.shape == (len(x), len(z)))
    tmp = -0.5 * dot(dot(z - x, inv(sigma)), z - x)
    res = 1.0 / power(2.0 * pi, len(z) / 2.0) * (1.0 / sqrt(det(sigma))) * exp(tmp)
    return res