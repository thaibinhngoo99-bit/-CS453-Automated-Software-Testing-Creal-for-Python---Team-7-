@pytest.mark.parametrize('gamma, slopes, knot_spacings', [(2.0, np.array([3, 1, 3, 4]), np.array([0.3, 0.2, 0.35, 0.15]))])
@pytest.mark.parametrize('hybridize', [True, False])
def test_piecewise_linear(gamma: float, slopes: np.ndarray, knot_spacings: np.ndarray, hybridize: bool) -> None:
    """
    Test to check that minimizing the CRPS recovers the quantile function
    """
    num_samples = 500
    gammas = mx.nd.zeros((num_samples,)) + gamma
    slopess = mx.nd.zeros((num_samples, len(slopes))) + mx.nd.array(slopes)
    knot_spacingss = mx.nd.zeros((num_samples, len(knot_spacings))) + mx.nd.array(knot_spacings)
    pwl_sqf = PiecewiseLinear(gammas, slopess, knot_spacingss)
    samples = pwl_sqf.sample()
    gamma_init = gamma - START_TOL_MULTIPLE * TOL * gamma
    slopes_init = slopes - START_TOL_MULTIPLE * TOL * slopes
    knot_spacings_init = knot_spacings
    mid = len(slopes) // 2
    knot_spacings_init[:mid] = knot_spacings[:mid] - START_TOL_MULTIPLE * TOL * knot_spacings[:mid]
    knot_spacings_init[mid:] = knot_spacings[mid:] + START_TOL_MULTIPLE * TOL * knot_spacings[mid:]
    init_biases = [gamma_init, slopes_init, knot_spacings_init]
    gamma_hat, slopes_hat, knot_spacings_hat = maximum_likelihood_estimate_sgd(PiecewiseLinearOutput(len(slopes)), samples, init_biases=init_biases, hybridize=hybridize, learning_rate=PositiveFloat(0.01), num_epochs=PositiveInt(20))
    quantile_levels = np.arange(0.1, 1.0, 0.1)
    pwl_sqf_hat = PiecewiseLinear(mx.nd.array(gamma_hat), mx.nd.array(slopes_hat).expand_dims(axis=0), mx.nd.array(knot_spacings_hat).expand_dims(axis=0))
    quantiles_hat = np.squeeze(pwl_sqf_hat.quantile(mx.nd.array(quantile_levels).expand_dims(axis=0), axis=1).asnumpy())
    quantiles = np.squeeze(pwl_sqf.quantile(mx.nd.array(quantile_levels).expand_dims(axis=0).repeat(axis=0, repeats=num_samples), axis=1).asnumpy()[0, :])
    for ix, (quantile, quantile_hat) in enumerate(zip(quantiles, quantiles_hat)):
        assert np.abs(quantile_hat - quantile) < TOL * quantile, f"quantile level {quantile_levels[ix]} didn't match: q = {quantile}, q_hat = {quantile_hat}"