def wrap_compute_conv2d(topi_compute, need_data_layout=False, need_out_layout=False, has_groups=False, need_auto_scheduler_layout=False):
    """Wrap conv2d topi compute"""

    def _compute_conv2d(attrs, inputs, out_type):
        padding = get_const_tuple(attrs.padding)
        strides = get_const_tuple(attrs.strides)
        dilation = get_const_tuple(attrs.dilation)
        data_layout = attrs.get_str('data_layout')
        out_layout = attrs.get_str('out_layout')
        out_dtype = attrs.out_dtype
        auto_scheduler_rewritten_layout = get_auto_scheduler_rewritten_layout(attrs)
        out_dtype = inputs[0].dtype if out_dtype in ('same', '') else out_dtype
        args = [inputs[0], inputs[1], strides, padding, dilation]
        if has_groups:
            args.append(attrs.groups)
        if need_data_layout:
            args.append(data_layout)
        if need_out_layout:
            args.append(out_layout)
        args.append(out_dtype)
        if need_auto_scheduler_layout:
            args.append(auto_scheduler_rewritten_layout)
        return [topi_compute(*args)]
    return _compute_conv2d