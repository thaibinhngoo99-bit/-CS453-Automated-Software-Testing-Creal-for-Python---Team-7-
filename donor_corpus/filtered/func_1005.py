def wrap_compute_argsort(topi_compute):
    """Wrap argsort topi compute"""

    def _compute_argsort(attrs, inputs, _):
        axis = get_const_int(attrs.axis)
        is_ascend = bool(get_const_int(attrs.is_ascend))
        dtype = attrs.dtype
        return [topi_compute(inputs[0], axis=axis, is_ascend=is_ascend, dtype=dtype)]
    return _compute_argsort