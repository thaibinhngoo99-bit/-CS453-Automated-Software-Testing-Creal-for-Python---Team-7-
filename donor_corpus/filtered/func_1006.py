@override_native_generic_func('argsort_strategy')
def argsort_strategy(attrs, inputs, out_type, target):
    """argsort generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_argsort(topi.argsort), wrap_topi_schedule(topi.generic.schedule_argsort), name='argsort.generic')
    return strategy