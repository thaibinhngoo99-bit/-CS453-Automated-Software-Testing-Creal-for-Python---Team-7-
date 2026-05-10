def wrap_compute_scatter_nd(topi_compute):
    """Wrap scatter_nd topi compute"""

    def _compute_scatter_nd(attrs, inputs, _):
        return [topi_compute(inputs[0], inputs[1], attrs.out_shape)]
    return _compute_scatter_nd