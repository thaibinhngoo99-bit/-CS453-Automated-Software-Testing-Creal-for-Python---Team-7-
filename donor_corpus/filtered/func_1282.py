def _exp_integral_func_shifting(lambd, lower, upper, model):

    def raw_integral(x):
        return z.exp(lambd * model._shift_x(x)) / lambd
    lower_int = raw_integral(x=lower)
    upper_int = raw_integral(x=upper)
    integral = upper_int - lower_int
    return integral