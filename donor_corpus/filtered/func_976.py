def get_conv2d_in_channels(data_shape, data_layout):
    """Get conv2d input channels"""
    data_shape = get_const_tuple(data_shape)
    if len(data_shape) == 4:
        idx = data_layout.find('C')
        assert idx >= 0, 'Invalid conv2d data layout {}'.format(data_layout)
        return data_shape[idx]
    if re.match('NCHW\\d*c', data_layout):
        return data_shape[1] * data_shape[4]
    raise ValueError('Unknown conv2d data layout {}'.format(data_layout))