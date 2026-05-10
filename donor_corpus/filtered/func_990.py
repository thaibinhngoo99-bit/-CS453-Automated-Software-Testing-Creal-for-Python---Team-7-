@override_native_generic_func('conv3d_transpose_strategy')
def conv3d_transpose_strategy(attrs, inputs, out_type, target):
    """conv3d_transpose generic strategy"""
    logger.warning('conv3d_transpose is not optimized for this platform.')
    layout = attrs.data_layout
    dilation = get_const_tuple(attrs.dilation)
    groups = attrs.groups
    assert layout == 'NCDHW', 'only support ncdhw for now'
    assert dilation == (1, 1, 1), 'not support dilate now'
    assert groups == 1, 'only support groups == 1 for now'
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_conv3d_transpose(topi.nn.conv3d_transpose_ncdhw), wrap_topi_schedule(topi.generic.schedule_conv3d_transpose_ncdhw), name='conv3d_transpose_ncdhw.generic')
    return strategy