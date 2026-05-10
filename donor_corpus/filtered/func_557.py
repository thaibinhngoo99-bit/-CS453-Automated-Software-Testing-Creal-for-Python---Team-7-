def test_iminuit_frozen(pars):
    pars['y'].frozen = True
    factors, info, minuit = optimize_iminuit(function=fcn, parameters=pars)
    assert info['success']
    assert_allclose(pars['x'].value, 2, rtol=0.0001)
    assert_allclose(pars['y'].value, 310000.0)
    assert_allclose(pars['z'].value, 4e-05, rtol=0.0001)
    assert_allclose(fcn(pars), 0.111112, rtol=1e-05)
    assert minuit.list_of_fixed_param() == ['par_001_y']