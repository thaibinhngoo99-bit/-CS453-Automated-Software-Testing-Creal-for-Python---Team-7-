@override_native_generic_func('dense_strategy')
def dense_strategy(attrs, inputs, out_type, target):
    """dense generic strategy"""
    logger.warning('dense is not optimized for this platform.')
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_dense(topi.nn.dense), wrap_topi_schedule(topi.generic.schedule_dense), name='dense.generic')
    return strategy