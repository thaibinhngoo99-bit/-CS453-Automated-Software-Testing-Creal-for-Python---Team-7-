def interpolate1d(x, values, tangents):
    """
    Returns:
        Returns the interpolated or extrapolated values for each query point,
        depending on whether or not the query lies within the span of the spline.
    """
    assert torch.is_tensor(x)
    assert torch.is_tensor(values)
    assert torch.is_tensor(tangents)
    float_dtype = x.dtype
    assert values.dtype == float_dtype
    assert tangents.dtype == float_dtype
    assert len(values.shape) == 1
    assert len(tangents.shape) == 1
    assert values.shape[0] == tangents.shape[0]
    x_lo = torch.floor(torch.clamp(x, torch.as_tensor(0), values.shape[0] - 2)).type(torch.int64)
    x_hi = x_lo + 1
    t = x - x_lo.type(float_dtype)
    t_sq = t ** 2
    t_cu = t * t_sq
    h01 = -2.0 * t_cu + 3.0 * t_sq
    h00 = 1.0 - h01
    h11 = t_cu - t_sq
    h10 = h11 - t_sq + t
    value_before = tangents[0] * t + values[0]
    value_after = tangents[-1] * (t - 1.0) + values[-1]
    neighbor_values_lo = values[x_lo]
    neighbor_values_hi = values[x_hi]
    neighbor_tangents_lo = tangents[x_lo]
    neighbor_tangents_hi = tangents[x_hi]
    value_mid = neighbor_values_lo * h00 + neighbor_values_hi * h01 + neighbor_tangents_lo * h10 + neighbor_tangents_hi * h11
    return torch.where(t < 0.0, value_before, torch.where(t > 1.0, value_after, value_mid))