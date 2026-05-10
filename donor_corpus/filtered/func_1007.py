def wrap_compute_topk(topi_compute):
    """Wrap topk compute"""

    def _compute_topk(attrs, inputs, out_type):
        if attrs.k is not None:
            k = attrs.k
        else:
            k = inputs[1]
        axis = get_const_int(attrs.axis)
        ret_type = attrs.ret_type
        is_ascend = bool(get_const_int(attrs.is_ascend))
        dtype = attrs.dtype
        out = topi_compute(inputs[0], k, axis, ret_type, is_ascend, dtype)
        out = out if isinstance(out, list) else [out]
        return out
    return _compute_topk