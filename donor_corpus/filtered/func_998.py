@override_native_generic_func('dilation2d_strategy')
def dilation2d_strategy(attrs, inputs, out_type, target):
    """dilation2d_strategy generic strategy"""
    logger.warning('dilation2d_strategy is not optimized for this platform.')
    strategy = _op.OpStrategy()
    dilations = get_const_tuple(attrs.dilations)
    layout = attrs.data_layout
    kernel_layout = attrs.kernel_layout
    assert layout in ['NCHW', 'NHWC']
    dilation_h, dilation_w = dilations
    if dilation_h < 1 or dilation_w < 1:
        raise ValueError('dilation should be positive value')
    if layout == 'NCHW':
        assert kernel_layout == 'IHW'
        strategy.add_implementation(wrap_compute_dilation2d(topi.image.dilation2d_nchw), wrap_topi_schedule(topi.generic.schedule_dilation2d_nchw), name='dilation2d_nchw.generic')
    elif layout == 'NHWC':
        assert kernel_layout == 'HWI'
        strategy.add_implementation(wrap_compute_dilation2d(topi.image.dilation2d_nhwc), wrap_topi_schedule(topi.generic.schedule_dilation2d_nhwc), name='dilation2d_nhwc.generic')
    else:
        raise RuntimeError('Unsupported dilation2d layout {}'.format(layout))
    return strategy