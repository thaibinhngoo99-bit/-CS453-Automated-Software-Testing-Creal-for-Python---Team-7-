@ops.RegisterGradient('BlockLSTM')
def _BlockLSTMGrad(op, *grad):
    """Gradient for BlockLSTM."""
    seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b = op.inputs
    i, cs, f, o, ci, co, h = op.outputs
    cs_grad = grad[1]
    h_grad = grad[6]
    x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad, b_grad = gen_lstm_ops.block_lstm_grad(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole=op.get_attr('use_peephole'))
    return [None, x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad, b_grad]