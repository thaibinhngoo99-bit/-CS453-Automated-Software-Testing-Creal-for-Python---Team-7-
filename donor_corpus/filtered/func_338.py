@autotvm.task.register('topi_x86_conv2d_NCHWc_int8')
def _topi_nn_conv2d_NCHWc_int8(*args, **kwargs):
    assert not kwargs, 'Do not support kwargs in template function call'
    args = deserialize_args(args)
    if len(args) == 7:
        data, kernel, strides, padding, dilation, origin_layout, dtype = args
    else:
        assert len(args) == 8
        data, kernel, strides, padding, dilation, origin_layout, out_layout, dtype = args
    raw_data_shape = get_const_tuple(data.shape)
    raw_kernel_shape = get_const_tuple(kernel.shape)
    cfg = get_config()
    _create_tuning_space_int8(cfg, data, kernel, strides, padding, dilation, origin_layout)
    ic_bn, oc_bn, ow_bn = (cfg['tile_ic'].size[-1], cfg['tile_oc'].size[-1], cfg['tile_ow'].size[-1])
    data_layout = 'NCHW%dc' % ic_bn
    out_layout = 'NCHW%dc' % oc_bn
    new_data_shape = (raw_data_shape[0], raw_data_shape[1] // ic_bn, raw_data_shape[2], raw_data_shape[3], ic_bn)
    n_elems = 4
    new_kernel_shape = (raw_kernel_shape[0] // oc_bn, raw_kernel_shape[1] // ic_bn, raw_kernel_shape[2], raw_kernel_shape[3], ic_bn // n_elems, oc_bn, n_elems)
    new_data = tvm.placeholder(new_data_shape, data.dtype)
    new_kernel = tvm.placeholder(new_kernel_shape, kernel.dtype)
    C = _declaration_conv_NCHWc_int8(cfg, new_data, new_kernel, strides, padding, dilation, data_layout, out_layout, dtype)
    s = _schedule_conv2d_NCHWc_int8(cfg, [C])
    return (s, [new_data, new_kernel, C])