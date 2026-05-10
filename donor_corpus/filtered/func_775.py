@contextlib.contextmanager
def with_torch_seed(seed):
    assert isinstance(seed, int)
    rng_state = torch.get_rng_state()
    cuda_rng_state = torch.cuda.get_rng_state()
    set_torch_seed(seed)
    yield
    torch.set_rng_state(rng_state)
    torch.cuda.set_rng_state(cuda_rng_state)