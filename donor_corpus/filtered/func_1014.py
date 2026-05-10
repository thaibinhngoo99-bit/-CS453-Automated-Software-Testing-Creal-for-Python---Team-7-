@override_native_generic_func('get_valid_counts_strategy')
def get_valid_counts_strategy(attrs, inputs, out_type, target):
    """get_valid_counts generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_get_valid_counts(topi.vision.get_valid_counts), wrap_topi_schedule(topi.generic.schedule_get_valid_counts), name='get_valid_counts.generic')
    return strategy