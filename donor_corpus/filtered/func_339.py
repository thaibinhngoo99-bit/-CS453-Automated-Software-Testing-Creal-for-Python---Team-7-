@autotvm.register_topi_schedule(generic.schedule_conv2d_NCHWc_int8, 'cpu', ['direct'])
def _schedule_conv2d_NCHWc_int8(cfg, outs):
    """Create schedule for tensors"""
    s = tvm.create_schedule([x.op for x in outs])
    scheduled_ops = []

    def traverse(op):
        """Traverse operators from computation graph"""
        if tag.is_broadcast(op.tag):
            if op not in s.outputs:
                s[op].compute_inline()
            for tensor in op.input_tensors:
                if isinstance(tensor.op, tvm.tensor.ComputeOp) and tensor.op not in scheduled_ops:
                    traverse(tensor.op)
        if 'conv2d_NCHWc_int8' in op.tag:
            conv_out = op.output(0)
            kernel = conv_out.op.input_tensors[1]
            data_vec = conv_out.op.input_tensors[0]
            data = data_vec.op.input_tensors[0] if isinstance(data_vec.op, tvm.tensor.ComputeOp) and 'pad' not in data_vec.op.tag else data_vec
            if isinstance(data.op, tvm.tensor.ComputeOp) and 'pad' in data.op.tag:
                data_pad = data
                data = data_pad.op.input_tensors[0]
            args = [s, cfg, data_vec, conv_out, outs[0]]
            target = tvm.target.current_target(allow_none=False)
            _, _, kh, kw, _, _, _ = get_const_tuple(kernel.shape)
            if kh == 1 and kw == 1:
                conv2d_avx_1x1._schedule_conv_NCHWc_int8(*args)
            else:
                conv2d_avx_common._schedule_conv_NCHWc_int8(*args)
        scheduled_ops.append(op)
    traverse(outs[0].op)
    return s