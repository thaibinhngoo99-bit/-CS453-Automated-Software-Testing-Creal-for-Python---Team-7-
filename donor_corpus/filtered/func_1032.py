def wrap_compute_argwhere(topi_compute):
    """wrap argwhere topi compute"""

    def _compute_argwhere(attrs, inputs, out_type):
        output_shape = []
        for s in out_type.shape:
            if hasattr(s, 'value'):
                output_shape.append(s)
            else:
                output_shape.append(te.var('any_dim', 'int32'))
        new_output_type = ir.TensorType(output_shape, 'int32')
        return [topi_compute(new_output_type, inputs[0])]
    return _compute_argwhere