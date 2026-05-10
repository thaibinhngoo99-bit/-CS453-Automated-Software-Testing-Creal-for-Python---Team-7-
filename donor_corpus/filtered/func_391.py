def simpleMultivariateNormalPdf(z, detFactorSigma):
    """ Assuming z has been transformed to a mean of zero and an identity matrix of covariances.
    Needs to provide the determinant of the factorized (real) covariance matrix. """
    dim = len(z)
    return exp(-0.5 * dot(z, z)) / (power(2.0 * pi, dim / 2.0) * detFactorSigma)