def wrap_compute_scatter(topi_compute):
    """Wrap scatter topi compute"""

    def _compute_scatter(attrs, inputs, _):
        return [topi_compute(inputs[0], inputs[1], inputs[2], axis=attrs.axis)]
    return _compute_scatter