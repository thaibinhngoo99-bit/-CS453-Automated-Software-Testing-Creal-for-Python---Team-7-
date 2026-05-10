@override_native_generic_func('conv3d_strategy')
def conv3d_strategy(attrs, inputs, out_type, target):
    """conv3d generic strategy"""
    logger.warning('conv3d is not optimized for this platform.')
    strategy = _op.OpStrategy()
    layout = attrs.data_layout
    if layout == 'NCDHW':
        strategy.add_implementation(wrap_compute_conv3d(topi.nn.conv3d_ncdhw), wrap_topi_schedule(topi.generic.schedule_conv3d_ncdhw), name='conv3d_ncdhw.generic')
    elif layout == 'NDHWC':
        strategy.add_implementation(wrap_compute_conv3d(topi.nn.conv3d_ndhwc), wrap_topi_schedule(topi.generic.schedule_conv3d_ndhwc), name='conv3d_ndhwc.generic')
    else:
        raise ValueError('Not support this layout {} yet'.format(layout))
    return strategy