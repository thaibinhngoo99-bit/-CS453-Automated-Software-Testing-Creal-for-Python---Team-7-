@override_native_generic_func('scatter_add_strategy')
def scatter_add_strategy(attrs, outs, out_type, target):
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_scatter(topi.scatter_add), wrap_topi_schedule(topi.generic.schedule_scatter), name='scatter_add.generic')
    return strategy