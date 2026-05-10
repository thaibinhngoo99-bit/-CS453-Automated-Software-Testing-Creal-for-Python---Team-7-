@pytest.mark.timeout(10)
def test_multivariate_gaussian() -> None:
    num_samples = 2000
    dim = 2
    mu = np.arange(0, dim) / float(dim)
    L_diag = np.ones((dim,))
    L_low = 0.1 * np.ones((dim, dim)) * np.tri(dim, k=-1)
    L = np.diag(L_diag) + L_low
    Sigma = L.dot(L.transpose())
    distr = MultivariateGaussian(mu=mx.nd.array(mu), L=mx.nd.array(L))
    samples = distr.sample(num_samples)
    mu_hat, L_hat = maximum_likelihood_estimate_sgd(MultivariateGaussianOutput(dim=dim), samples, init_biases=None, hybridize=False, learning_rate=PositiveFloat(0.01), num_epochs=PositiveInt(10))
    distr = MultivariateGaussian(mu=mx.nd.array([mu_hat]), L=mx.nd.array([L_hat]))
    Sigma_hat = distr.variance[0].asnumpy()
    assert np.allclose(mu_hat, mu, atol=0.1, rtol=0.1), f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.allclose(Sigma_hat, Sigma, atol=0.1, rtol=0.1), f'Sigma did not match: sigma = {Sigma}, sigma_hat = {Sigma_hat}'