def wrap_compute_deformable_conv2d(topi_compute):
    """wrap deformable_conv2d topi compute"""

    def _compute_deformable_conv2d(attrs, inputs, out_dtype):
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        dilation = get_const_tuple(attrs.dilation)
        deformable_groups = attrs.deformable_groups
        groups = attrs.groups
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        out = topi_compute(inputs[0], inputs[1], inputs[2], strides, padding, dilation, deformable_groups, groups, out_dtype)
        return [out]
    return _compute_deformable_conv2d