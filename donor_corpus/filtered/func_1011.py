def wrap_compute_multibox_transform_loc(topi_compute):
    """Wrap multibox_transform_loc compute"""

    def _compute_multibox_transform_loc(attrs, inputs, _):
        """Compute definition of multibox_detection"""
        clip = bool(get_const_int(attrs.clip))
        threshold = get_const_float(attrs.threshold)
        variances = get_float_tuple(attrs.variances)
        return topi_compute(inputs[0], inputs[1], inputs[2], clip, threshold, variances)
    return _compute_multibox_transform_loc