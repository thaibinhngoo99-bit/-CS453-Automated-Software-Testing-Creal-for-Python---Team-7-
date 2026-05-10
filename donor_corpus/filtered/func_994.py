@override_native_generic_func('conv1d_strategy')
def conv1d_strategy(attrs, inputs, out_type, target):
    """conv1d generic strategy"""
    logger.warning('conv1d is not optimized for this platform.')
    layout = attrs.data_layout
    dilation = get_const_tuple(attrs.dilation)
    if dilation[0] < 1:
        raise ValueError('dilation should be a positive value')
    strategy = _op.OpStrategy()
    if layout == 'NCW':
        strategy.add_implementation(wrap_compute_conv1d(topi.nn.conv1d_ncw), wrap_topi_schedule(topi.generic.schedule_conv1d_ncw), name='conv1d_ncw.generic')
    elif layout == 'NWC':
        strategy.add_implementation(wrap_compute_conv1d(topi.nn.conv1d_nwc), wrap_topi_schedule(topi.generic.schedule_conv1d_nwc), name='conv1d_nwc.generic')
    else:
        raise ValueError('Unsupported conv1d layout {}'.format(layout))
    return strategy