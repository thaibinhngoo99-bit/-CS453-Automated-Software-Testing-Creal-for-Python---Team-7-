def get_conv2d_out_channels(kernel_shape, kernel_layout):
    """Get conv2d output channels"""
    kernel_shape = get_const_tuple(kernel_shape)
    if len(kernel_shape) == 4:
        idx = kernel_layout.find('O')
        assert idx >= 0, 'Invalid conv2d kernel layout {}'.format(kernel_layout)
        return kernel_shape[idx]
    if re.match('OIHW\\d*i\\d*o', kernel_layout):
        return kernel_shape[0] * kernel_shape[5]
    if re.match('OIHW\\d*o', kernel_layout):
        return kernel_shape[0] * kernel_shape[4]
    raise ValueError('Unknown conv2d kernel layout {}'.format(kernel_layout))