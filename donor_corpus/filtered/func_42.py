def switch_init(tensor: torch.Tensor, s: float=0.1, mean: float=0) -> torch.Tensor:
    fan_in, fan_out = torch.nn.init._calculate_fan_in_and_fan_out(tensor)
    std = math.sqrt(s / fan_in)
    return torch.nn.init.trunc_normal_(tensor=tensor, mean=mean, std=std)