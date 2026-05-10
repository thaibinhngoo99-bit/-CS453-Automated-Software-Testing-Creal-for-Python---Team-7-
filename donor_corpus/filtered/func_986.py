@override_native_generic_func('deformable_conv2d_strategy')
def deformable_conv2d_strategy(attrs, inputs, out_type, target):
    """deformable_conv2d generic strategy"""
    layout = attrs.data_layout
    strategy = _op.OpStrategy()
    if layout == 'NCHW':
        strategy.add_implementation(wrap_compute_deformable_conv2d(topi.nn.deformable_conv2d_nchw), wrap_topi_schedule(topi.generic.schedule_deformable_conv2d_nchw), name='deformable_conv2d_nchw.generic')
    elif layout == 'NHWC':
        strategy.add_implementation(wrap_compute_deformable_conv2d(topi.nn.deformable_conv2d_nhwc), naive_schedule, name='deformable_conv2d_nhwc.generic')
    else:
        raise RuntimeError('Layout %s is not supported in deformable conv2d' % layout)
    return strategy