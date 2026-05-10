@override_native_generic_func('softmax_strategy')
def softmax_strategy(attrs, inputs, out_type, target):
    """softmax generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_softmax(topi.nn.softmax), wrap_topi_schedule(topi.generic.schedule_softmax), name='softmax.generic')
    return strategy