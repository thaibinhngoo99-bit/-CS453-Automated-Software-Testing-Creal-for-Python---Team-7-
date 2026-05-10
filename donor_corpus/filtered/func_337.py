def _create_tuning_space_int8(cfg, data, kernel, strides, padding, dilation, layout):
    """Create schedule configuration from input arguments"""
    dshape = get_const_tuple(data.shape)
    kshape = get_const_tuple(kernel.shape)
    pat = re.compile('NCHW.+(\\d+)c')
    if layout == 'NCHW':
        n, ic, h, w = dshape
        oc, _, kh, kw = kshape
    elif layout == 'NHWC':
        n, h, w, ic = dshape
        kh, kw, oc, _ = kshape
    elif pat.match(layout) is not None:
        n, ic_chunk, h, w, ic_bn = dshape
        target = tvm.target.current_target(allow_none=False)
        oc_chunk, k_ic, kh, kw, k_ic_f, oc_bn, k_ic_s = kshape
        ic = ic_chunk * ic_bn
        assert ic == k_ic * k_ic_f * k_ic_s
        oc = oc_chunk * oc_bn
    else:
        raise ValueError('Not support this layout {} with schedule template.'.format(layout))
    is_kernel_1x1 = kh == 1 and kw == 1
    ph, pw = padding if isinstance(padding, (tuple, list)) else (padding, padding)
    sh, sw = strides if isinstance(strides, (tuple, list)) else (strides, strides)
    oh = (h - kh + 2 * ph) // sh + 1
    ow = (w - kw + 2 * pw) // sw + 1
    cfg.define_split('tile_ic', ic, num_outputs=2, filter=lambda y: y.size[-1] % 4 == 0)
    cfg.define_split('tile_oc', oc, num_outputs=2, filter=lambda y: y.size[-1] % 16 == 0)
    cfg.define_split('tile_ow', ow, num_outputs=2, filter=lambda y: y.size[-1] <= 64)
    if is_kernel_1x1:
        cfg.define_knob('tile_oh', [1, 2] if oh > 1 else [1])
    else:
        cfg.define_knob('unroll_kw', [True, False])