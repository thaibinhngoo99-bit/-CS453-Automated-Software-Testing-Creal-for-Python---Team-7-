@autotvm.register_topi_schedule(generic.schedule_conv2d_nhwc_pack, 'cpu', ['direct'])
def schedule_conv2d_nhwc_pack(cfg, outs):
    """Create schedule for tensors"""
    s = tvm.create_schedule([x.op for x in outs])
    output_op = outs[0].op
    scheduled_ops = []

    def traverse(op):
        """Traverse operators from computation graph"""
        if tag.is_broadcast(op.tag):
            if op not in s.outputs:
                s[op].compute_inline()
            elif len(op.axis) == 4:
                n, h, w, c = op.axis
                fused = s[op].fuse(n, h, w)
                s[op].parallel(fused)
                s[op].vectorize(c)
            for tensor in op.input_tensors:
                if isinstance(tensor.op, tvm.tensor.ComputeOp) and tensor.op not in scheduled_ops:
                    traverse(tensor.op)
        if 'conv2d_nhwc_pack_int8' in op.tag:
            conv_out = op.output(0)
            kernel = conv_out.op.input_tensors[1]
            data_vec = conv_out.op.input_tensors[0]
            data = data_vec.op.input_tensors[0] if isinstance(data_vec.op, tvm.tensor.ComputeOp) and 'pad' not in data_vec.op.tag else data_vec
            if isinstance(data.op, tvm.tensor.ComputeOp) and 'pad' in data.op.tag:
                data_pad = data
                data = data_pad.op.input_tensors[0]
            args = [s, cfg, data_vec, conv_out, outs[0]]
            if data.dtype == 'uint8':
                kh, kw, _, _, _ = get_const_tuple(kernel.shape)
                if kh == 1 and kw == 1:
                    conv2d_avx_1x1._schedule_conv_nhwc_pack_int8(*args)
                else:
                    raise ValueError('Only support 1x1 kernel with schedule_conv2d_nhwc_pack.')
            else:
                raise ValueError('Not support this data type {} with schedule_conv2d_nhwc_pack. Only support int8'.format(data.dtype))
        scheduled_ops.append(op)
    traverse(output_op)
    return s