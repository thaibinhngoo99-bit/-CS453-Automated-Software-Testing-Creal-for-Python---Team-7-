@override_native_generic_func('argwhere_strategy')
def argwhere_strategy(attrs, inputs, out_type, target):
    """argwhere generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_argwhere(topi.argwhere), wrap_topi_schedule(topi.generic.schedule_argwhere), name='argwhere.generic')
    return strategy