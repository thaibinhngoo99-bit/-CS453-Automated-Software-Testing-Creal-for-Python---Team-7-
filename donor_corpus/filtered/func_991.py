def wrap_compute_conv3d(topi_compute, need_layout=False):
    """wrap conv3d topi compute"""

    def _compute_conv3d(attrs, inputs, out_type):
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        dilation = get_const_tuple(attrs.dilation)
        groups = attrs.groups
        layout = attrs.data_layout
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        dilation_d, dilation_h, dilation_w = dilation
        if dilation_d < 1 or dilation_h < 1 or dilation_w < 1:
            raise ValueError('Dilation should be positive value')
        if groups != 1:
            raise ValueError('Not support arbitrary group number for conv3d')
        if need_layout:
            out = topi_compute(inputs[0], inputs[1], strides, padding, dilation, layout, out_dtype)
        else:
            out = topi_compute(inputs[0], inputs[1], strides, padding, dilation, out_dtype)
        return [out]
    return _compute_conv3d