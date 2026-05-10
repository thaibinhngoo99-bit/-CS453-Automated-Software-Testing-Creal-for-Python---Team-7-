@pytest.mark.parametrize('mu_alpha', [(2.5, 0.7)])
@pytest.mark.parametrize('hybridize', [True, False])
def test_neg_binomial(mu_alpha: Tuple[float, float], hybridize: bool) -> None:
    """
    Test to check that maximizing the likelihood recovers the parameters
    """
    mu, alpha = mu_alpha
    mus = mx.nd.zeros((NUM_SAMPLES,)) + mu
    alphas = mx.nd.zeros((NUM_SAMPLES,)) + alpha
    neg_bin_distr = NegativeBinomial(mu=mus, alpha=alphas)
    samples = neg_bin_distr.sample()
    init_biases = [inv_softplus(mu - START_TOL_MULTIPLE * TOL * mu), inv_softplus(alpha + START_TOL_MULTIPLE * TOL * alpha)]
    mu_hat, alpha_hat = maximum_likelihood_estimate_sgd(NegativeBinomialOutput(), samples, hybridize=hybridize, init_biases=init_biases, num_epochs=PositiveInt(15))
    assert np.abs(mu_hat - mu) < TOL * mu, f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.abs(alpha_hat - alpha) < TOL * alpha, f'alpha did not match: alpha = {alpha}, alpha_hat = {alpha_hat}'