@pytest.mark.skip('this test fails when run locally')
@pytest.mark.parametrize('lam_1, lam_2', [(0.1, 0.01)])
@pytest.mark.parametrize('mu, sigma', [(-1.5, 0.5)])
@pytest.mark.parametrize('hybridize', [True])
def test_box_cox_tranform(lam_1: float, lam_2: float, mu: float, sigma: float, hybridize: bool):
    """
    Test to check that maximizing the likelihood recovers the parameters
    """
    lamdas_1 = mx.nd.zeros((NUM_SAMPLES,)) + lam_1
    lamdas_2 = mx.nd.zeros((NUM_SAMPLES,)) + lam_2
    transform = InverseBoxCoxTransform(lamdas_1, lamdas_2)
    mus = mx.nd.zeros((NUM_SAMPLES,)) + mu
    sigmas = mx.nd.zeros((NUM_SAMPLES,)) + sigma
    gausian_distr = Gaussian(mus, sigmas)
    trans_distr = TransformedDistribution(gausian_distr, transform)
    samples = trans_distr.sample()
    init_biases = [mu - START_TOL_MULTIPLE * TOL * mu, inv_softplus(sigma - START_TOL_MULTIPLE * TOL * sigma), lam_1 - START_TOL_MULTIPLE * TOL * lam_1, inv_softplus(lam_2 - START_TOL_MULTIPLE * TOL * lam_2)]
    mu_hat, sigma_hat, lam_1_hat, lam_2_hat = maximum_likelihood_estimate_sgd(TransformedDistributionOutput(GaussianOutput(), InverseBoxCoxTransformOutput(lb_obs=lam_2, fix_lambda_2=True)), samples, init_biases=init_biases, hybridize=hybridize, learning_rate=PositiveFloat(0.01), num_epochs=PositiveInt(18))
    assert np.abs(lam_1_hat - lam_1) < TOL * lam_1, f'lam_1 did not match: lam_1 = {lam_1}, lam_1_hat = {lam_1_hat}'
    assert np.abs(mu_hat - mu) < TOL * np.abs(mu), f'mu did not match: mu = {mu}, mu_hat = {mu_hat}'
    assert np.abs(sigma_hat - sigma) < TOL * sigma, f'sigma did not match: sigma = {sigma}, sigma_hat = {sigma_hat}'