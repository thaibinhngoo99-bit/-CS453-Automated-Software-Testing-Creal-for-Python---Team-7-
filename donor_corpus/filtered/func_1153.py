@pytest.mark.parametrize('num_bins', [6])
@pytest.mark.parametrize('bin_probabilites', [np.array([0.3, 0.1, 0.05, 0.2, 0.1, 0.25])])
@pytest.mark.parametrize('hybridize', [True, False])
def test_binned_likelihood(num_bins: float, bin_probabilites: np.ndarray, hybridize: bool):
    """
    Test to check that maximizing the likelihood recovers the parameters
    """
    bin_prob = mx.nd.array(bin_probabilites)
    bin_center = mx.nd.array(np.logspace(-1, 1, num_bins))
    bin_probs = mx.nd.zeros((NUM_SAMPLES, num_bins)) + bin_prob
    bin_centers = mx.nd.zeros((NUM_SAMPLES, num_bins)) + bin_center
    distr = Binned(bin_probs, bin_centers)
    samples = distr.sample()
    bin_prob_init = mx.nd.random_uniform(1 - TOL, 1 + TOL, num_bins) * bin_prob
    bin_prob_init = bin_prob_init / bin_prob_init.sum()
    init_biases = [bin_prob_init]
    bin_prob_hat, = maximum_likelihood_estimate_sgd(BinnedOutput(list(bin_center.asnumpy())), samples, init_biases=init_biases, hybridize=hybridize, learning_rate=PositiveFloat(0.05), num_epochs=PositiveInt(25))
    assert all(mx.nd.abs(mx.nd.array(bin_prob_hat) - bin_prob) < TOL * bin_prob), f'bin_prob did not match: bin_prob = {bin_prob}, bin_prob_hat = {bin_prob_hat}'