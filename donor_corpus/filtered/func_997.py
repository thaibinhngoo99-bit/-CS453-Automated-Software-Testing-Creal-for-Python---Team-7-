def wrap_compute_dilation2d(topi_compute, need_data_layout=False):
    """Wrap dilation2d topi compute"""

    def _compute_dilation2d(attrs, inputs, out_type):
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        dilations = get_const_tuple(attrs.dilations)
        data_layout = attrs.get_str('data_layout')
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        args = [inputs[0], inputs[1], strides, padding, dilations]
        if need_data_layout:
            args.append(data_layout)
        args.append(out_dtype)
        return [topi_compute(*args)]
    return _compute_dilation2d