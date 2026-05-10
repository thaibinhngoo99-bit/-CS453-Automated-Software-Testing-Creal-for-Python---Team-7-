def wrap_compute_sparse_dense(topi_compute):
    """wrap sparse dense topi compute"""

    def _compute_sparse_dense(attrs, inputs, out_type):
        return [topi_compute(inputs[0], inputs[1], inputs[2], inputs[3], attrs['sparse_lhs'])]
    return _compute_sparse_dense