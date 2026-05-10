def wrap_compute_conv1d_transpose(topi_compute):
    """wrap conv1d_transpose topi compute"""

    def _compute_conv1d_tranpsoe(attrs, inputs, out_type):
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        output_padding = get_const_tuple(attrs.output_padding)
        out = topi_compute(inputs[0], inputs[1], strides, padding, out_dtype, output_padding)
        return [out]
    return _compute_conv1d_tranpsoe