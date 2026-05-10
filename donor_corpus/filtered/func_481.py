def test_GaussianProcessRegressionSklearn_3():
    """All predictive distributions.

    Linear noisy function, linear kernel + white noise kernel.
    The optimized noise level is expected to go to its true value.
    """
    kernel = skl.gaussian_process.kernels.DotProduct(sigma_0=0, sigma_0_bounds='fixed') + skl.gaussian_process.kernels.WhiteKernel(noise_level=1, noise_level_bounds=(1e-05, 100000.0))
    gpr = GaussianProcessRegressionSklearn(kernel=kernel, rng=1)
    n, nlsd = (100, 0.5)
    data = smlb.TabularData(data=np.ones(shape=(n, 1)) * 2, labels=np.ones(shape=n) * 3)
    data = smlb.LabelNoise(noise=smlb.NormalNoise(stddev=nlsd, rng=1)).fit(data).apply(data)
    preds = gpr.fit(data).apply(data)
    assert preds.has_signal_part and preds.has_noise_part
    conf, noise = (preds.signal_part, preds.noise_part)
    assert np.allclose(conf.mean, np.ones(n) * 3, atol=0.1)
    assert np.allclose(conf.stddev, np.ones(n) * nlsd, atol=0.1)
    assert (preds.mean == conf.mean).all()
    assert np.allclose(preds.stddev, np.sqrt(np.square(conf.stddev) + np.square(nlsd)), atol=0.1)
    assert np.allclose(noise.mean, np.zeros(shape=n))
    assert np.allclose(noise.stddev, nlsd, atol=0.1)