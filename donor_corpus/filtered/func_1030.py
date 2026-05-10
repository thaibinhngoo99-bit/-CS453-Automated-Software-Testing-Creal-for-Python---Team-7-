def wrap_compute_correlation(topi_compute):
    """wrap correlation topi compute"""

    def _compute_correlation(attrs, inputs, out_type):
        kernel_size = attrs.kernel_size
        max_displacement = attrs.max_displacement
        stride1 = attrs.stride1
        stride2 = attrs.stride2
        padding = get_const_tuple(attrs.padding)
        is_multiply = attrs.is_multiply
        return [topi_compute(inputs[0], inputs[1], kernel_size, max_displacement, stride1, stride2, padding, is_multiply)]
    return _compute_correlation