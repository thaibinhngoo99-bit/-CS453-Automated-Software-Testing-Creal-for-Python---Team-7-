def wrap_compute_conv1d(topi_compute):
    """wrap conv1d topi compute"""

    def _compute_conv1d(attrs, inputs, out_type):
        """Compute definition of conv1d"""
        strides = get_const_tuple(attrs.strides)
        padding = get_const_tuple(attrs.padding)
        dilation = get_const_tuple(attrs.dilation)
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        return [topi_compute(inputs[0], inputs[1], strides, padding, dilation, out_dtype)]
    return _compute_conv1d