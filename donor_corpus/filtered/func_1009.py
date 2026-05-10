def wrap_compute_multibox_prior(topi_compute):
    """Wrap multibox_prior compute"""

    def _compute_multibox_prior(attrs, inputs, _):
        """Compute definition of multibox_prior"""
        sizes = get_float_tuple(attrs.sizes)
        ratios = get_float_tuple(attrs.ratios)
        steps = get_float_tuple(attrs.steps)
        offsets = get_float_tuple(attrs.offsets)
        clip = bool(get_const_int(attrs.clip))
        return [topi_compute(inputs[0], sizes, ratios, steps, offsets, clip)]
    return _compute_multibox_prior