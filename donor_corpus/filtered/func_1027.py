@override_native_generic_func('bitserial_conv2d_strategy')
def bitserial_conv2d_strategy(attrs, inputs, out_type, target):
    """bitserial_conv2d generic strategy"""
    logger.warning('bitserial_conv2d is not optimized for this platform.')
    strategy = _op.OpStrategy()
    layout = attrs.data_layout
    if layout == 'NCHW':
        strategy.add_implementation(wrap_compute_bitserial_conv2d(topi.nn.bitserial_conv2d_nchw), wrap_topi_schedule(topi.generic.schedule_bitserial_conv2d_nchw), name='bitserial_conv2d_nchw.generic')
    elif layout == 'NHWC':
        strategy.add_implementation(wrap_compute_bitserial_conv2d(topi.nn.bitserial_conv2d_nhwc), wrap_topi_schedule(topi.generic.schedule_bitserial_conv2d_nhwc), name='bitserial_conv2d_nhwc.generic')
    else:
        raise ValueError('Data layout {} not supported.'.format(layout))
    return strategy