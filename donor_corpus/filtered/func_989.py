def wrap_compute_conv3d_transpose(topi_compute):
    """wrap conv3d_transpose topi compute"""

    def compute_conv3d_transpose(attrs, inputs, out_dtype):
        """Compute definition of conv3d_transpose"""
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        output_padding = get_const_tuple(attrs.output_padding)
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        out = topi_compute(inputs[0], inputs[1], strides, padding, out_dtype, output_padding)
        return [out]
    return compute_conv3d_transpose