def wrap_compute_batch_matmul(topi_compute):
    """wrap batch_matmul topi compute"""

    def _compute_batch_matmul(attrs, inputs, out_type):
        return [topi_compute(inputs[0], inputs[1], out_type.shape)]
    return _compute_batch_matmul