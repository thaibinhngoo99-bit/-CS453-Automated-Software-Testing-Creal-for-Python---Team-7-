def _exp_integral_from_any_to_any(limits, params, model):
    lambda_ = params['lambda']
    lower, upper = limits.rect_limits
    integral = _exp_integral_func_shifting(lambd=lambda_, lower=lower, upper=upper, model=model)
    return integral[0]