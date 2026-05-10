def wrap_compute_bitserial_conv2d(topi_compute):
    """wrap bitserial_conv2d topi compute"""

    def compute_bitserial_conv2d(attrs, inputs, out_dtype):
        """Compute definition for bitserial conv2d."""
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        activation_bits = attrs.activation_bits
        weight_bits = attrs.weight_bits
        pack_dtype = attrs.pack_dtype
        out_dtype = attrs.out_dtype
        unipolar = attrs.unipolar
        return [topi_compute(inputs[0], inputs[1], strides, padding, activation_bits, weight_bits, pack_dtype, out_dtype, unipolar)]
    return compute_bitserial_conv2d