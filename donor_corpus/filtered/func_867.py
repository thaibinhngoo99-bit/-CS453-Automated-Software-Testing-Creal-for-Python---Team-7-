def get_partition_init(shape):
    shape = torch.as_tensor(shape)
    base1 = (2.25 * shape - 4.5) / (torch.abs(shape - 2) + 0.25) + shape + 2
    base2 = 5.0 / 18.0 * log_safe(4 * shape - 15) + 8
    return torch.where(shape < 4, base1, base2)