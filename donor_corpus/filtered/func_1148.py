@pytest.mark.parametrize('mu', [1.0])
@pytest.mark.parametrize('hybridize', [True, False])
def test_deterministic_l1(mu: float, hybridize: bool) -> None:
    """
    Test to check that maximizing the likelihood recovers the parameters.
    This tests uses the Laplace distribution with fixed variance and sample mean.
    This essentially reduces to determistic L1.
    """
    mu = mu
    mus = mx.nd.zeros(NUM_SAMPLES) + mu

    class LaplaceFixedVarianceOutput(LaplaceOutput):

        @classmethod
        def domain_map(cls, F, mu, b):
            b = 0.1 * F.ones_like(b)
            return (mu.squeeze(axis=-1), b.squeeze(axis=-1))
    deterministic_distr = Laplace(mu=mus, b=0.1 * mx.nd.ones_like(mus))
    samples = deterministic_distr.sample()
    mu_hat, _ = maximum_likelihood_estimate_sgd(LaplaceFixedVarianceOutput(), samples, init_biases=[3 * mu, 0.1], learning_rate=PositiveFloat(0.001), hybridize=hybridize)
    assert np.abs(mu_hat - mu) < TOL * mu, f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'