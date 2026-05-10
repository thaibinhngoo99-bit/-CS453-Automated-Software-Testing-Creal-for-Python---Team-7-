@override_native_generic_func('scatter_nd_strategy')
def scatter_nd_strategy(attrs, inputs, out_type, target):
    """scatter_nd generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_scatter_nd(topi.scatter_nd), wrap_topi_schedule(topi.generic.schedule_extern), name='scatter_nd.generic')
    return strategy