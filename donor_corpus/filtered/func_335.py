def _get_default_config_int8(cfg, data, kernel, strides, padding, out_dtype, is_depthwise=False, layout='NCHW'):
    """
    Get default schedule config for the workload
    """
    assert not is_depthwise, 'Depthwise Int8 not supported'
    wkl = _get_conv2d_workload(data, kernel, strides, padding, out_dtype, layout)
    is_kernel_1x1 = wkl.hkernel == 1 and wkl.wkernel == 1
    if is_kernel_1x1:
        conv2d_generic.fallback_schedule_cpu_1x1_int8(cfg, wkl, int32_lanes=16, num_int8_elements=4)
    else:
        conv2d_generic.fallback_schedule_cpu_common_int8(cfg, wkl, int32_lanes=16, num_int8_elements=4)