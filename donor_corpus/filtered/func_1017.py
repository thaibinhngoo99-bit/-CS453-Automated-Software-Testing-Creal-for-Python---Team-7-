def wrap_compute_roi_align(topi_compute):
    """wrap roi_align topi compute"""

    def _compute_roi_align(attrs, inputs, out_type):
        assert attrs.layout == 'NCHW'
        pooled_size = get_const_tuple(attrs.pooled_size)
        return [topi_compute(inputs[0], inputs[1], pooled_size=pooled_size, spatial_scale=attrs.spatial_scale, sample_ratio=attrs.sample_ratio)]
    return _compute_roi_align