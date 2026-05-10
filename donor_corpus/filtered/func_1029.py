@override_native_generic_func('bitserial_dense_strategy')
def bitserial_dense_strategy(attrs, inputs, out_type, target):
    """bitserial_dense generic strategy"""
    logger.warning('bitserial_dense is not optimized for this platform.')
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_bitserial_dense(topi.nn.bitserial_dense), wrap_topi_schedule(topi.generic.schedule_bitserial_dense), name='bitserial_dense.generic')
    return strategy