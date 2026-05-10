def _lstm_block_cell(x, cs_prev, h_prev, w, b, wci=None, wcf=None, wco=None, forget_bias=None, cell_clip=None, use_peephole=None, name=None):
    """Computes the LSTM cell forward propagation for 1 time step.

  This implementation uses 1 weight matrix and 1 bias vector, and there's an
  optional peephole connection.

  This kernel op implements the following mathematical equations:

  ```python
  xh = [x, h_prev]
  [i, ci, f, o] = xh * w + b
  f = f + forget_bias

  if not use_peephole:
    wci = wcf = wco = 0

  i = sigmoid(cs_prev * wci + i)
  f = sigmoid(cs_prev * wcf + f)
  ci = tanh(ci)

  cs = ci .* i + cs_prev .* f
  cs = clip(cs, cell_clip)

  o = sigmoid(cs * wco + o)
  co = tanh(cs)
  h = co .* o
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`.
      The input to the LSTM cell, shape (batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      Value of the cell state at previous time step.
    h_prev: A `Tensor`. Must have the same type as `x`.
      Output of the previous cell at previous time step.
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    forget_bias: An optional `float`. Defaults to `1`. The forget gate bias.
    cell_clip: An optional `float`. Defaults to `-1` (no clipping).
      Value to clip the 'cs' value to. Disable by setting to negative value.
    use_peephole: An optional `bool`. Defaults to `False`.
      Whether to use peephole weights.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (i, cs, f, o, ci, co, h).
    i: A `Tensor`. Has the same type as `x`. The input gate.
    cs: A `Tensor`. Has the same type as `x`. The cell state before the tanh.
    f: A `Tensor`. Has the same type as `x`. The forget gate.
    o: A `Tensor`. Has the same type as `x`. The output gate.
    ci: A `Tensor`. Has the same type as `x`. The cell input.
    co: A `Tensor`. Has the same type as `x`. The cell after the tanh.
    h: A `Tensor`. Has the same type as `x`. The output h vector.

  Raises:
    ValueError: If cell_size is None.
  """
    if wci is None:
        cell_size = cs_prev.get_shape().with_rank(2)[1].value
        if cell_size is None:
            raise ValueError('cell_size from `cs_prev` should not be None.')
        wci = array_ops.constant(0, dtype=dtypes.float32, shape=[cell_size])
        wcf = wci
        wco = wci
    return gen_lstm_ops.lstm_block_cell(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b, forget_bias=forget_bias, cell_clip=cell_clip if cell_clip is not None else -1, use_peephole=use_peephole, name=name)