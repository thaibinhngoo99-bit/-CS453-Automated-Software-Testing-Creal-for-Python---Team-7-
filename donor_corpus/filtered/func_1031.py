@override_native_generic_func('correlation_strategy')
def correlation_strategy(attrs, inputs, out_type, target):
    """correlation generic strategy"""
    logger.warning('correlation is not optimized for this platform.')
    layout = attrs.layout
    assert layout == 'NCHW', 'Only support NCHW layout'
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_correlation(topi.nn.correlation_nchw), wrap_topi_schedule(topi.generic.schedule_correlation_nchw), name='correlation.generic')
    return strategy