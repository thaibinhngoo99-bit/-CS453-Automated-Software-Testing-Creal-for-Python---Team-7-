@pytest.mark.parametrize('mu, sigma', [(1.0, 0.1)])
@pytest.mark.parametrize('hybridize', [True, False])
def test_gaussian_likelihood(mu: float, sigma: float, hybridize: bool):
    """
    Test to check that maximizing the likelihood recovers the parameters
    """
    mus = mx.nd.zeros((NUM_SAMPLES,)) + mu
    sigmas = mx.nd.zeros((NUM_SAMPLES,)) + sigma
    distr = Gaussian(mus, sigmas)
    samples = distr.sample()
    init_biases = [mu - START_TOL_MULTIPLE * TOL * mu, inv_softplus(sigma - START_TOL_MULTIPLE * TOL * sigma)]
    mu_hat, sigma_hat = maximum_likelihood_estimate_sgd(GaussianOutput(), samples, init_biases=init_biases, hybridize=hybridize, learning_rate=PositiveFloat(0.001), num_epochs=PositiveInt(5))
    assert np.abs(mu_hat - mu) < TOL * mu, f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.abs(sigma_hat - sigma) < TOL * sigma, f'alpha did not match: sigma = {sigma}, sigma_hat = {sigma_hat}'