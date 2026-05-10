@override_native_generic_func('conv2d_strategy')
def conv2d_strategy(attrs, inputs, out_type, target):
    """conv2d generic strategy"""
    logger.warning('conv2d is not optimized for this platform.')
    strategy = _op.OpStrategy()
    data, kernel = inputs
    dilation = get_const_tuple(attrs.dilation)
    groups = attrs.groups
    layout = attrs.data_layout
    kernel_layout = attrs.kernel_layout
    dilation_h, dilation_w = dilation
    if dilation_h < 1 or dilation_w < 1:
        raise ValueError('dilation should be positive value')
    if groups == 1:
        if layout == 'NCHW':
            assert kernel_layout == 'OIHW'
            strategy.add_implementation(wrap_compute_conv2d(topi.nn.conv2d_nchw), wrap_topi_schedule(topi.generic.schedule_conv2d_nchw), name='conv2d_nchw.generic')
        elif layout == 'NHWC':
            assert kernel_layout == 'HWIO'
            strategy.add_implementation(wrap_compute_conv2d(topi.nn.conv2d_nhwc), wrap_topi_schedule(topi.generic.schedule_conv2d_nhwc), name='conv2d_nhwc.generic')
        elif layout == 'HWCN':
            assert kernel_layout == 'HWIO'
            strategy.add_implementation(wrap_compute_conv2d(topi.nn.conv2d_hwcn), wrap_topi_schedule(topi.generic.schedule_conv2d_hwcn), name='conv2d_hwcn.generic')
        else:
            raise RuntimeError('Unsupported conv2d layout {}'.format(layout))
    elif is_depthwise_conv2d(data.shape, layout, kernel.shape, kernel_layout, groups):
        if layout == 'NCHW':
            assert kernel_layout == 'OIHW'
            strategy.add_implementation(wrap_compute_conv2d(topi.nn.depthwise_conv2d_nchw), wrap_topi_schedule(topi.generic.schedule_depthwise_conv2d_nchw), name='depthwise_conv2d_nchw.generic')
        elif layout == 'NHWC':
            assert kernel_layout == 'HWOI'
            strategy.add_implementation(wrap_compute_conv2d(topi.nn.depthwise_conv2d_nhwc), wrap_topi_schedule(topi.generic.schedule_depthwise_conv2d_nhwc), name='depthwise_conv2d_nhwc.generic')
        else:
            raise RuntimeError('Unsupported depthwise_conv2d layout {}'.format(layout))
    elif layout == 'NCHW':
        assert kernel_layout == 'OIHW'
        strategy.add_implementation(wrap_compute_conv2d(topi.nn.group_conv2d_nchw, has_groups=True), wrap_topi_schedule(topi.generic.schedule_group_conv2d_nchw), name='group_conv2d_nchw.generic')
    elif layout == 'NHWC':
        assert kernel_layout == 'HWIO'
        strategy.add_implementation(wrap_compute_conv2d(topi.nn.group_conv2d_nhwc, has_groups=True), wrap_topi_schedule(topi.generic.schedule_group_conv2d_nhwc), name='group_conv2d_nhwc.generic')
    else:
        raise RuntimeError('Unsupported group_conv2d layout {}'.format(layout))
    return strategy