@override_native_generic_func('conv2d_transpose_strategy')
def conv2d_transpose_strategy(attrs, inputs, out_type, target):
    """conv2d_transpose generic strategy"""
    logger.warning('conv2d_transpose is not optimized for this platform.')
    layout = attrs.data_layout
    dilation = get_const_tuple(attrs.dilation)
    groups = attrs.groups
    assert layout == 'NCHW', 'only support nchw for now'
    assert dilation == (1, 1), 'not support dilate now'
    assert groups == 1, 'only support groups == 1 for now'
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_conv2d_transpose(topi.nn.conv2d_transpose_nchw), wrap_topi_schedule(topi.generic.schedule_conv2d_transpose_nchw), name='conv2d_transpose_nchw.generic')
    return strategy