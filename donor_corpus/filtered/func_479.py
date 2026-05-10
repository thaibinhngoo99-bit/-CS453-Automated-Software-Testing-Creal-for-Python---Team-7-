def test_GaussianProcessRegressionSklearn_1():
    """Simple examples."""
    kernel = skl.gaussian_process.kernels.DotProduct(sigma_0=0, sigma_0_bounds='fixed')
    gpr = GaussianProcessRegressionSklearn(kernel=kernel, optimizer=None, rng=1)
    train_data = smlb.TabularData(data=np.array([[-1], [1]]), labels=np.array([-1, 1]))
    valid_data = smlb.TabularData(data=np.array([[-2], [-1], [0], [1], [2]]))
    preds = gpr.fit(train_data).apply(valid_data)
    mean, stddev = (preds.mean, preds.stddev)
    assert np.allclose(mean, [-2, -1, 0, 1, 2])
    assert stddev[0] > stddev[1] > stddev[2] < stddev[3] < stddev[4]