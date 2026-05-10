@override_native_generic_func('scatter_strategy')
def scatter_strategy(attrs, outs, out_type, target):
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_scatter(topi.scatter), wrap_topi_schedule(topi.generic.schedule_scatter), name='scatter.generic')
    return strategy