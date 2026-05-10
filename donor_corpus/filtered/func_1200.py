@ops.RegisterGradient('LSTMBlockCell')
def _LSTMBlockCellGrad(op, *grad):
    """Gradient for LSTMBlockCell."""
    x, cs_prev, h_prev, w, wci, wcf, wco, b = op.inputs
    i, cs, f, o, ci, co, _ = op.outputs
    _, cs_grad, _, _, _, _, h_grad = grad
    batch_size = x.get_shape().with_rank(2)[0].value
    if batch_size is None:
        batch_size = -1
    input_size = x.get_shape().with_rank(2)[1].value
    if input_size is None:
        raise ValueError('input_size from `x` should not be None.')
    cell_size = cs_prev.get_shape().with_rank(2)[1].value
    if cell_size is None:
        raise ValueError('cell_size from `cs_prev` should not be None.')
    cs_prev_grad, dicfo, wci_grad, wcf_grad, wco_grad = gen_lstm_ops.lstm_block_cell_grad(x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, cs_grad, h_grad, use_peephole=op.get_attr('use_peephole'))
    xh_grad = math_ops.matmul(dicfo, w, transpose_b=True)
    x_grad = array_ops.slice(xh_grad, (0, 0), (batch_size, input_size))
    x_grad.get_shape().merge_with(x.get_shape())
    h_prev_grad = array_ops.slice(xh_grad, (0, input_size), (batch_size, cell_size))
    h_prev_grad.get_shape().merge_with(h_prev.get_shape())
    xh = array_ops.concat([x, h_prev], 1)
    w_grad = math_ops.matmul(xh, dicfo, transpose_a=True)
    w_grad.get_shape().merge_with(w.get_shape())
    b_grad = nn_ops.bias_add_grad(dicfo)
    b_grad.get_shape().merge_with(b.get_shape())
    return (x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad, b_grad)