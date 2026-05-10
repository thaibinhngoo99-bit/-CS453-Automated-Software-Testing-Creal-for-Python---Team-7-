def _block_lstm(seq_len_max, x, w, b, cs_prev=None, h_prev=None, wci=None, wcf=None, wco=None, forget_bias=None, cell_clip=None, use_peephole=None, name=None):
    """TODO(williamchan): add doc.

  Args:
    seq_len_max: A `Tensor` of type `int64`.
    x: A list of at least 1 `Tensor` objects of the same type in: `float32`.
    w: A `Tensor`. Must have the same type as `x`.
    b: A `Tensor`. Must have the same type as `x`.
    cs_prev: A `Tensor`. Must have the same type as `x`.
    h_prev: A `Tensor`. Must have the same type as `x`.
    wci: A `Tensor`. Must have the same type as `x`.
    wcf: A `Tensor`. Must have the same type as `x`.
    wco: A `Tensor`. Must have the same type as `x`.
    forget_bias: An optional `float`. Defaults to `1`.
    cell_clip: An optional `float`. Defaults to `-1` (no clipping).
    use_peephole: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (i, cs, f, o, ci, co, h).
    i: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.
    cs: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.
    f: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.
    o: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.
    ci: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.
    co: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.
    h: A list with the same number of `Tensor` objects as `x` of `Tensor`
    objects of the same type as x.

  Raises:
    ValueError: If `b` does not have a valid shape.
  """
    batch_size = x[0].get_shape().with_rank(2)[0].value
    cell_size4 = b.get_shape().with_rank(1)[0].value
    if cell_size4 is None:
        raise ValueError('`b` shape must not be None.')
    cell_size = cell_size4 / 4
    zero_state = None
    if cs_prev is None or h_prev is None:
        zero_state = array_ops.constant(0, dtype=dtypes.float32, shape=[batch_size, cell_size])
    if cs_prev is None:
        cs_prev = zero_state
    if h_prev is None:
        h_prev = zero_state
    if wci is None:
        wci = array_ops.constant(0, dtype=dtypes.float32, shape=[cell_size])
        wcf = wci
        wco = wci
    i, cs, f, o, ci, co, h = gen_lstm_ops.block_lstm(seq_len_max=seq_len_max, x=array_ops.stack(x), cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b, forget_bias=forget_bias, cell_clip=cell_clip if cell_clip is not None else -1, name=name, use_peephole=use_peephole)
    return (array_ops.unstack(i), array_ops.unstack(cs), array_ops.unstack(f), array_ops.unstack(o), array_ops.unstack(ci), array_ops.unstack(co), array_ops.unstack(h))