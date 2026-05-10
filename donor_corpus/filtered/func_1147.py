@pytest.mark.parametrize('mu', [6.0])
@pytest.mark.parametrize('hybridize', [True, False])
def test_deterministic_l2(mu: float, hybridize: bool) -> None:
    """
    Test to check that maximizing the likelihood recovers the parameters.
    This tests uses the Gaussian distribution with fixed variance and sample mean.
    This essentially reduces to determistic L2.
    """
    mu = mu
    mus = mx.nd.zeros(NUM_SAMPLES) + mu
    deterministic_distr = Gaussian(mu=mus, sigma=0.1 * mx.nd.ones_like(mus))
    samples = deterministic_distr.sample()

    class GaussianFixedVarianceOutput(GaussianOutput):

        @classmethod
        def domain_map(cls, F, mu, sigma):
            sigma = 0.1 * F.ones_like(sigma)
            return (mu.squeeze(axis=-1), sigma.squeeze(axis=-1))
    mu_hat, _ = maximum_likelihood_estimate_sgd(GaussianFixedVarianceOutput(), samples, init_biases=[3 * mu, 0.1], hybridize=hybridize, num_epochs=PositiveInt(1))
    assert np.abs(mu_hat - mu) < TOL * mu, f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'