def wrap_compute_softmax(topi_compute):
    """Wrap softmax topi compute"""

    def _compute_softmax(attrs, inputs, out_type):
        axis = attrs.get_int('axis')
        return [topi_compute(inputs[0], axis)]
    return _compute_softmax