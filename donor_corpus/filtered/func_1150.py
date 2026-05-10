@pytest.mark.timeout(10)
@pytest.mark.parametrize('mu_b', [(3.3, 0.7)])
@pytest.mark.parametrize('hybridize', [True, False])
def test_laplace(mu_b: Tuple[float, float], hybridize: bool) -> None:
    """
    Test to check that maximizing the likelihood recovers the parameters
    """
    mu, b = mu_b
    mus = mx.nd.zeros((NUM_SAMPLES,)) + mu
    bs = mx.nd.zeros((NUM_SAMPLES,)) + b
    laplace_distr = Laplace(mu=mus, b=bs)
    samples = laplace_distr.sample()
    init_biases = [mu - START_TOL_MULTIPLE * TOL * mu, inv_softplus(b + START_TOL_MULTIPLE * TOL * b)]
    mu_hat, b_hat = maximum_likelihood_estimate_sgd(LaplaceOutput(), samples, hybridize=hybridize, init_biases=init_biases)
    assert np.abs(mu_hat - mu) < TOL * mu, f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.abs(b_hat - b) < TOL * b, f'b did not match: b = {b}, b_hat = {b_hat}'