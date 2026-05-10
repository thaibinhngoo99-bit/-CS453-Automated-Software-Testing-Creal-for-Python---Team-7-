@pytest.mark.timeout(10)
def test_lowrank_multivariate_gaussian() -> None:
    num_samples = 2000
    dim = 2
    rank = 1
    mu = np.arange(0, dim) / float(dim)
    D = np.eye(dim) * (np.arange(dim) / dim + 0.5)
    W = np.sqrt(np.ones((dim, rank)) * 0.2)
    Sigma = D + W.dot(W.transpose())
    distr = LowrankMultivariateGaussian(mu=mx.nd.array([mu]), D=mx.nd.array([np.diag(D)]), W=mx.nd.array([W]), dim=dim, rank=rank)
    assert np.allclose(distr.variance[0].asnumpy(), Sigma, atol=0.1, rtol=0.1), f'did not match: sigma = {Sigma}, sigma_hat = {distr.variance[0]}'
    samples = distr.sample(num_samples).squeeze().asnumpy()
    mu_hat, D_hat, W_hat = maximum_likelihood_estimate_sgd(LowrankMultivariateGaussianOutput(dim=dim, rank=rank), samples, learning_rate=PositiveFloat(0.01), num_epochs=PositiveInt(10), init_biases=None, hybridize=False)
    distr = LowrankMultivariateGaussian(dim=dim, rank=rank, mu=mx.nd.array([mu_hat]), D=mx.nd.array([D_hat]), W=mx.nd.array([W_hat]))
    Sigma_hat = distr.variance.asnumpy()
    assert np.allclose(mu_hat, mu, atol=0.2, rtol=0.1), f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.allclose(Sigma_hat, Sigma, atol=0.1, rtol=0.1), f'alpha did not match: sigma = {Sigma}, sigma_hat = {Sigma_hat}'