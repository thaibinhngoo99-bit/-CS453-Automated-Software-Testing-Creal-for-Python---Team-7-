@override_native_generic_func('depthwise_conv2d_NCHWc_strategy')
def depthwise_conv2d_NCHWc_strategy(attrs, inputs, out_type, target):
    """depthwise_conv2d generic strategy"""
    logger.warning('depthwise_conv2d_NCHWc is not optimized for this platform.')
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_conv2d(topi.nn.depthwise_conv2d_NCHWc, True, True), wrap_topi_schedule(topi.generic.schedule_depthwise_conv2d_NCHWc), name='depthwise_conv2d_NCHWc.generic')
    return strategy