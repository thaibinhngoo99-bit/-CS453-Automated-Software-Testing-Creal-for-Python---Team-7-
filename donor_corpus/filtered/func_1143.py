@pytest.mark.parametrize('mu, sigma, nu', [(2.3, 0.7, 6.0)])
@pytest.mark.parametrize('hybridize', [True, False])
def test_studentT_likelihood(mu: float, sigma: float, nu: float, hybridize: bool) -> None:
    """
    Test to check that maximizing the likelihood recovers the parameters
    """
    mus = mx.nd.zeros((NUM_SAMPLES,)) + mu
    sigmas = mx.nd.zeros((NUM_SAMPLES,)) + sigma
    nus = mx.nd.zeros((NUM_SAMPLES,)) + nu
    distr = StudentT(mus, sigmas, nus)
    samples = distr.sample()
    init_bias = [mu - START_TOL_MULTIPLE * TOL * mu, inv_softplus(sigma - START_TOL_MULTIPLE * TOL * sigma), inv_softplus(nu - 2)]
    mu_hat, sigma_hat, nu_hat = maximum_likelihood_estimate_sgd(StudentTOutput(), samples, init_biases=init_bias, hybridize=hybridize, num_epochs=PositiveInt(10), learning_rate=PositiveFloat(0.01))
    assert np.abs(mu_hat - mu) < TOL * mu, f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.abs(sigma_hat - sigma) < TOL * sigma, f'sigma did not match: sigma = {sigma}, sigma_hat = {sigma_hat}'
    assert np.abs(nu_hat - nu) < TOL * nu, 'nu0 did not match: nu0 = %s, nu_hat = %s' % (nu, nu_hat)