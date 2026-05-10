def set_torch_seed(seed):
    assert isinstance(seed, int)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)