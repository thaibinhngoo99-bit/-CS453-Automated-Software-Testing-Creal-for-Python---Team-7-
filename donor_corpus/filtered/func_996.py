@override_native_generic_func('conv1d_transpose_strategy')
def conv1d_transpose_strategy(attrs, inputs, out_type, target):
    """conv1d_transpose generic strategy"""
    logger.warning('conv1d_transpose is not optimized for this platform.')
    strategy = _op.OpStrategy()
    layout = attrs.data_layout
    dilation = get_const_tuple(attrs.dilation)
    groups = attrs.groups
    assert layout == 'NCW', 'conv1d_transpose ncw only supported'
    assert dilation == (1,), 'conv1d_transpose dilation is not supported'
    assert groups == 1, 'conv1d_transpose groups == 1 only supported'
    strategy.add_implementation(wrap_compute_conv1d_transpose(topi.nn.conv1d_transpose_ncw), wrap_topi_schedule(topi.generic.schedule_conv1d_transpose_ncw), name='conv1d_transpose_ncw.generic')
    return strategy