def test_iminuit_basic(pars):
    factors, info, minuit = optimize_iminuit(function=fcn, parameters=pars)
    assert info['success']
    assert_allclose(fcn(pars), 0, atol=1e-05)
    assert_allclose(pars['x'].value, 2, rtol=0.001)
    assert_allclose(pars['y'].value, 300000.0, rtol=0.001)
    assert_allclose(pars['z'].value, 4e-05, rtol=0.02)
    assert_allclose(factors, [2, 3, 4], rtol=0.001)
    assert_allclose(minuit.values['par_000_x'], 2, rtol=0.001)
    assert_allclose(minuit.values['par_001_y'], 3, rtol=0.001)
    assert_allclose(minuit.values['par_002_z'], 4, rtol=0.001)