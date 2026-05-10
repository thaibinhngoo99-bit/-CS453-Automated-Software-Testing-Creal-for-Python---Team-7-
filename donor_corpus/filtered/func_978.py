def is_depthwise_conv2d(data_shape, data_layout, kernel_shape, kernel_layout, groups):
    ic = get_conv2d_in_channels(data_shape, data_layout)
    oc = get_conv2d_out_channels(kernel_shape, kernel_layout)
    return ic == oc == groups