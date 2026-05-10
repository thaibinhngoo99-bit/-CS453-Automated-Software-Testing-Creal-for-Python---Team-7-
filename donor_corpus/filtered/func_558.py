def test_iminuit_limits(pars):
    pars['y'].min = 301000
    factors, info, minuit = optimize_iminuit(function=fcn, parameters=pars)
    assert info['success']
    assert_allclose(pars['x'].value, 2, rtol=0.01)
    assert_allclose(pars['y'].value, 301000, rtol=0.001)
    states = minuit.get_param_states()
    assert not states[0]['has_limits']
    y = states[1]
    assert y['has_limits']
    assert_allclose(y['lower_limit'], 3.01)