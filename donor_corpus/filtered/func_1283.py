def exp_icdf(x, params, model):
    lambd = params['lambda']
    x = z.unstack_x(x)
    x = model._shift_x(x)
    return znp.log(lambd * x) / lambd