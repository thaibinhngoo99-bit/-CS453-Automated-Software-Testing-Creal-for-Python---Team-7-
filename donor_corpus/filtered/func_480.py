def test_GaussianProcessRegressionSklearn_2():
    """All predictive distributions.

    Linear noise-free function, linear kernel + white noise kernel.
    The optimized noise level is expected to go to its lower bound.
    """
    kernel = skl.gaussian_process.kernels.DotProduct(sigma_0=0, sigma_0_bounds='fixed') + skl.gaussian_process.kernels.WhiteKernel(noise_level=0.1, noise_level_bounds=(1e-05, 1e-05))
    gpr = GaussianProcessRegressionSklearn(kernel=kernel, rng=1)
    n = 100
    train_data = smlb.TabularData(data=np.ones(shape=(n, 1)) * 2, labels=np.ones(shape=n) * 3)
    valid_data = smlb.TabularData(data=train_data.samples())
    preds = gpr.fit(train_data).apply(valid_data)
    assert preds.has_signal_part and preds.has_noise_part
    conf, noise = (preds.signal_part, preds.noise_part)
    assert np.allclose(conf.mean, train_data.labels())
    assert np.allclose(conf.stddev, np.ones(n) * np.sqrt(1e-05), atol=0.001)
    assert (preds.mean == conf.mean).all()
    assert np.allclose(preds.stddev, np.ones(n) * np.sqrt(np.square(conf.stddev) + 1e-05))
    assert np.allclose(noise.mean, np.zeros(shape=n))
    assert np.allclose(noise.stddev, np.sqrt(1e-05))