@override_native_generic_func('conv2d_NCHWc_strategy')
def conv2d_NCHWc_strategy(attrs, inputs, out_type, target):
    """conv2d_NCHWc generic strategy"""
    logger.warning('conv2d_NCHWc is not optimized for this platform.')
    strategy = _op.OpStrategy()
    if inputs[0].dtype == 'int8' or inputs[0].dtype == 'uint8':
        strategy.add_implementation(wrap_compute_conv2d(topi.nn.conv2d_NCHWc_int8, True, True), wrap_topi_schedule(topi.generic.schedule_conv2d_NCHWc_int8), name='conv2d_NCHWc_int8.generic')
    else:
        strategy.add_implementation(wrap_compute_conv2d(topi.nn.conv2d_NCHWc, True, True), wrap_topi_schedule(topi.generic.schedule_conv2d_NCHWc), name='conv2d_NCHWc.generic')
    return strategy