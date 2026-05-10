def wrap_compute_dense(topi_compute):
    """wrap dense topi compute"""

    def _compute_dense(attrs, inputs, out_type):
        """Compute definition of dense"""
        out_dtype = attrs.out_dtype
        out_dtype = inputs[0].dtype if out_dtype == '' else out_dtype
        return [topi_compute(inputs[0], inputs[1], None, out_dtype)]
    return _compute_dense