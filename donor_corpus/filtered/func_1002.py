@override_native_generic_func('batch_matmul_strategy')
def batch_matmul_strategy(attrs, inputs, out_type, target):
    """batch_matmul generic strategy"""
    logger.warning('batch_matmul is not optimized for this platform.')
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_batch_matmul(topi.nn.batch_matmul), wrap_topi_schedule(topi.generic.schedule_batch_matmul), name='batch_matmul.generic')
    return strategy