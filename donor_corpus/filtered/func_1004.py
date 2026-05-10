@override_native_generic_func('sparse_dense_strategy')
def sparse_dense_strategy(attrs, inputs, out_type, target):
    """sparse dense generic strategy"""
    logger.warning('sparse dense is not optimized for this platform.')
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_sparse_dense(topi.nn.sparse_dense), wrap_topi_schedule(topi.generic.schedule_sparse_dense), name='sparse_dense.generic')
    return strategy