def get_partition(shape):
    shape = torch.as_tensor(shape)
    assert (shape >= 0).all()
    init = get_partition_init(shape)
    x_scale, values, tangents = load_spline_params()
    return interpolate1d(init * x_scale.to(init), values.to(init), tangents.to(init))